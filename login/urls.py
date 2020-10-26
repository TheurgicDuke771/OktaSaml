from django.conf.urls import url
from django.contrib import admin
from .views import attrs, index, metadata, sso
admin.autodiscover()

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^attrs/$', attrs, name='attrs'),
    url(r'^metadata/$', metadata, name='metadata'),
    url(r'^sso$', sso, name='sso')
]
