from django.db import models


# Create your models here.


class BOOK(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    isibm = models.CharField(max_length=50,unique=True)
    price = models.IntegerField()


