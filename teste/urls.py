from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url('', include('usuarios.urls')),
    url('admin/', admin.site.urls),
]
