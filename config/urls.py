from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

api_urlpatterns = [
    path('items/', include('items.urls')),
    path('reviews/', include('reviews.urls')),
    path('users/', include('users.urls')),
    path('carts/', include('carts.urls'))
]

urlpatterns = [
    path('api/v1/', include(api_urlpatterns)),
    path('admin/', admin.site.urls),
    path('api/v1/users/auth/login/', obtain_auth_token, name='login')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
