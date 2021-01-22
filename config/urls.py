from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

api_url = [
    path('items/', include('items.urls')),
    path('reviews/', include('reviews.urls')),
    path('users/', include('users.urls'))
]

urlpatterns = [
    path('api/v1/', include(api_url)),
    path('admin/', admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
