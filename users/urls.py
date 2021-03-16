from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from users.views import UserCurrentViewSet, UserRegViewSet

urlpatterns = [
    path('current/', UserCurrentViewSet.as_view(), name='current'),
    path('auth/register/', UserRegViewSet.as_view(), name='register'),
    path('auth/login/', obtain_auth_token, name='login')
]
