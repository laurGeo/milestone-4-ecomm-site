from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField(max_length=254, default='')
    event1 = models.CharField(max_length=254, default='')
    event2 = models.CharField(max_length=254, default='')
    event3 = models.CharField(max_length=254, default='')
    year = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    bidding_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name