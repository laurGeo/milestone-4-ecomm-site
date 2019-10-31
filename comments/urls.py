from django.conf.urls import url
from .views import create_comment, comment_detail

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', create_comment, name='create_comment'),
    url(r'^(?P<id>\d+)/$', comment_detail, name='comment_detail'),
]