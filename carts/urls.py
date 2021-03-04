from django.urls import path
from rest_framework.routers import DefaultRouter

from carts.views import CartViewSet, CartItemViewSet

router = DefaultRouter()
router.register('', CartViewSet, basename='carts')
router.register('items', CartItemViewSet, basename='cart_items')
urlpatterns = router.urls
