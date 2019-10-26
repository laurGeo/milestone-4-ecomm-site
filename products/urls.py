from django.conf.urls import url, include
from .views import all_products, view_specific_product

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^view/(?P<id>\d+)', view_specific_product, name='view_specific_product')
    ]