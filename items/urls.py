from rest_framework.routers import DefaultRouter

from .views import ItemViewSet

router = DefaultRouter()
router.register('', ItemViewSet, basename='user_items')
urlpatterns = router.urls
