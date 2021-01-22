from django.urls import path

from .views import get_review_view

urlpatterns = [
    path('<pk>', get_review_view)
]
