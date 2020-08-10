from django.db import models



# Create your models here.


class type(models.Model):
    name = models.CharField(max_length=255)

class book (models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    type = models.ForeignKey(type, on_delete=models.CASCADE)