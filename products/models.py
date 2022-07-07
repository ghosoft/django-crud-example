# -*- coding: utf-8 -*-
from django.db import models
import django.utils.timezone as timezone
import datetime 
from django.utils import timezone

class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description', blank=True)
    start_time = models.DateTimeField('Start Time', null=True, default=timezone.now)
    duration = models.DecimalField('Duration', decimal_places=1, max_digits=8)
    count = models.IntegerField('Count', default=1)
    department = models.TextField('Department', blank=True)
    person = models.TextField('Person', blank=True)
    created = models.DateTimeField('Created', auto_now_add=True)
    changed = models.DateTimeField('Changed', auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('product_edit', kwargs={'pk': self.pk})
    def get_time_left(self):
        timepass = (timezone.now() - self.start_time) / datetime.timedelta(hours=1)
        timeleft = float(self.duration) - timepass
        return round(timeleft, 1)
    

class Factory(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
