from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('products/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('cart/', CartView.as_view(), name='cart'),
]