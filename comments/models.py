from django.db import models
from django.utils import timezone


class Comment(models.Model):
   
    username = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    rate = models.CharField(max_length=10)