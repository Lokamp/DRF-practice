from django.urls import path

from .views import get_user_view

urlpatterns = [
    path('<pk>', get_user_view)
]
