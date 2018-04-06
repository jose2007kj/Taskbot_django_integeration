# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TravelPlan(models.Model):
    

    origin = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    start_date = models.CharField(max_length=20)
    n_adults= models.CharField(max_length=20)
    n_children= models.CharField(max_length=20)
    price= models.CharField(max_length=20)
    duration= models.CharField(max_length=20)
    end_date= models.CharField(max_length=20)
    n_adults= models.CharField(max_length=20)
    breakfast= models.BooleanField(default=False)
    wifi= models.BooleanField(default=False)
    spa= models.BooleanField(default=False)
    category= models.CharField(max_length=20)

