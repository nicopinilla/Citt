from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.views import debug

from apps.endpoints.urls import urlpatterns as endpoints_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', debug.default_urlconf),
]

urlpatterns += endpoints_urlpatterns
