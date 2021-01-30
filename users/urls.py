from django.urls import path

from users.views import UserCurrentViewSet, UserRegViewSet

urlpatterns = [
    path('current/', UserCurrentViewSet.as_view()),
    path('register/', UserRegViewSet.as_view())
]


# router = DefaultRouter()
# router.register('register', UserRegViewSet, basename='user_reg')
# router.register('current', UserCurrentViewSet, basename='user_current')
# urlpatterns = router.urls

