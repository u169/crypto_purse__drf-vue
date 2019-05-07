from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('purse.api.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('registration/', include('registration.urls')),
    path('', include('app.urls')),
]
