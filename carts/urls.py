from django.urls import path

from carts.views import CartViewSet

urlpatterns = [
    path('', CartViewSet.as_view()),
]
