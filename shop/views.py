from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, View

from .models import Notebook, Smartphone, Category, LatestProduct, Customer, Cart, CartProduct

from .mixins import CategoryDetailMixin, CartMixin


def test(request):
    categories = Category.objects.get_categories_for_left_sidebar()
    products = LatestProduct.objects.get_products_for_main_page()
    return render(request, 'templates/base.html', {'categories': categories})


class ProductDetailView(CartMixin, CategoryDetailMixin, DetailView):

    CT_MODEL_MODEL_CLASS = {
        'notebook': Notebook,
        'smartphone': Smartphone,
    }
    
    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'product'
    template_name = 'shop/product_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ct_model'] = self.model._meta.model_name
        return context


class HomePage(CartMixin, View):
    
    def get(self, request):
        categories = Category.objects.get_categories_for_left_sidebar()
        products = LatestProduct.objects.get_products_for_main_page(
            'notebook', 'smartphone', with_respect_to='notebook'
        )
        context = {
            'categories': categories,
            'products': products,
            'cart': self.cart,
        }
        return render(request, 'shop/shop.html', context)


class CategoryDetailView(CartMixin, CategoryDetailMixin, DetailView):

    model = Category
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'shop/category_detail.html'
    slug_url_kwarg = 'slug'


class AddToCartView(CartMixin, View):

    def get(self, request, *args, **kwargs):
        ct_model, product_slug = kwargs.get('ct_model'), kwargs.get('slug')
        content_type = ContentType.objects.get(model=ct_model)
        product = content_type.model_class().objects.get(slug=product_slug)
        cart_product, created = CartProduct.objects.get_or_create(
            user=self.cart.owner, cart=self.cart, content_type=content_type, object_id=product.id
        )
        if created:
            self.cart.products.add(cart_product)
        return HttpResponseRedirect('/cart/')


class CartView(CartMixin, View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.get_categories_for_left_sidebar()
        context = {
            'categories': categories,
            'cart': self.cart
        }
        return render(request, 'shop/cart.html', context)