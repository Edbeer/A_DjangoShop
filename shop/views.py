from django.shortcuts import render
from django.views.generic import DetailView, View

from .models import Notebook, Smartphone, Category, LatestProduct

from .mixins import CategoryDetailMixin


def test(request):
    categories = Category.objects.get_categories_for_left_sidebar()
    products = LatestProduct.objects.get_products_for_main_page()
    return render(request, 'templates/base.html', {'categories': categories})


class ProductDetailView(CategoryDetailMixin, DetailView):

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


class HomePage(View):
    
    def get(self, request):
        categories = Category.objects.get_categories_for_left_sidebar()
        products = LatestProduct.objects.get_products_for_main_page()
        return render(request, 'shop/shop.html', {'categories': categories, 'products': products})


class CategoryDetailView(CategoryDetailMixin, DetailView):

    model = Category
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'shop/category_detail.html'
    slug_url_kwarg = 'slug'