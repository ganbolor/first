#coding:utf-8

from django.db import models
from django.contrib.auth.models import User

# TODO: mod helbereer haruulax

#Хэсэг нэгж
class Department(models.Model):
    name = models.CharField(max_length=40)
    short_name = models.CharField(max_length=10)
    
    order = models.IntegerField()
    is_active = models.BooleanField()
    
    class Meta:
        ordering = ["name"]
        #verbose_name_plural = "oxen"

        
    