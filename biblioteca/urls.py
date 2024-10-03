from django.contrib import admin
from django.urls import path, include
from rest_framework.response import Response
from rest_framework.reverse import reverse

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_urls'),
    path('api/', include('core.urls'), name='core_urls'),
]