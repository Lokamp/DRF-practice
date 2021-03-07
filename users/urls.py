from django.urls import path

from users.views import UserCurrentViewSet, UserRegViewSet

urlpatterns = [
    path('current/', UserCurrentViewSet.as_view()),
    path('register/', UserRegViewSet.as_view())
]
