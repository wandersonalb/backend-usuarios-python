from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt   
from usuarios.views import MyView

app_name = 'usuarios'

urlpatterns = [
    url(r'usuarios/$', csrf_exempt(MyView.as_view()), name='get'),
    url(r'usuario/', csrf_exempt(MyView.as_view()), name='post')
]
