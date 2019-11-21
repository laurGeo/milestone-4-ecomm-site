from django.conf.urls import url
from products.views import view_specific_product
from .views import create_comment, comment_detail

urlpatterns = [
    #url(r'^(?P<id>\d+)/$', view_specific_product, name='create_comment'),
    url(r'^view/(?P<id>\d+)', create_comment, name='create_comment'),
    url(r'^(?P<id>\d+)/$', comment_detail, name='comment_detail'),
]