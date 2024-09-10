from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_urls'),
    path('api/', include('core.urls'), name='core_urls'),
]