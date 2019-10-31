from django.conf.urls import url
from .views import do_search, do_filter

urlpatterns = [
    url(r'^$', do_search, name='search'),
    url(r'^$', do_filter, name='filter'),
    ]