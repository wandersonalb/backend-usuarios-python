from django.conf.urls import url
from . import views

app_name = 'usuarios'

urlpatterns = [
    url(r'usuarios/', views.get, name="get"),
    url(r'usuario/?$', views.search, name='search'),
    url(r'usuario/', views.post, name="post")
]
