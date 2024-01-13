from django.db import models


# Create your models here.

class Mobile(models.Model):
    name=models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    software=models.CharField(max_length=200)
    modelnumber=models.IntegerField()


    def __str__(self):
        return self.name





