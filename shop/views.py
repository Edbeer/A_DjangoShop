from django.shortcuts import render
from django.views.generic import DetailView

from .models import Notebook, Smartphone, Category, CategoryManager


def test(request):
    categories = Category.objects.get_categories_for_left_sidebar()
    return render(request, 'shop/shop.html', {'categories': categories})


class ProductDetailView(DetailView):

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


def shop(request):
    categories = Category.objects.get_categories_for_left_sidebar()
    return render(request, 'shop/shop.html', {'categories': categories})


class CategoryDetailView(DetailView):

    model = Category
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'shop/category_detail.html'
    slug_url_kwarg = 'slug'