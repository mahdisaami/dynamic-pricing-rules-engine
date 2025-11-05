from django.urls import path

from cart.views import MakeCartItem

urlpatterns = [
    path('create/', MakeCartItem.as_view(), name='create-cart-item'),
]