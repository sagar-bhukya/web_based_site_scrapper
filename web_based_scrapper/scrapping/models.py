from django.db import models

# Create your models here.

class Link(models.Model):
    address=models.CharField(max_length=1000,null=True,blank=True) #some
    name=models.CharField(max_length=1000,null=True,blank=True) #some

    def __str__(self):
        return self.name
