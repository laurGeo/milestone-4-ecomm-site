from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

"""Comments for individual products on detailed view"""
class Comment(models.Model):
   
    username = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    rate = models.CharField(max_length=10)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    
    def __unicode__(self):
        return self.task
