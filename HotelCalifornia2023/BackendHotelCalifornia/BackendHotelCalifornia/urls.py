
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('hotel_auth.urls')), 
    path('api/', include('hotel_api.urls')), 
]
