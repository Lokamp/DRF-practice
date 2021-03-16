from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='Stepic DRF API',
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


api_urlpatterns = [
    path('items/', include('items.urls')),
    path('reviews/', include('reviews.urls')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('carts/', include('carts.urls')),
    path('orders/', include('orders.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0))
]

urlpatterns = [
    path('api/v1/', include(api_urlpatterns)),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
