from django.urls import path
from .views import *

urlpatterns = [
    path('', shop, name='shop'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
]