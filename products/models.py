# -*- coding: utf-8 -*-
from django.db import models

class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description', blank=True)
    start_time = models.DateTimeField('Start Time', auto_now_add=True)
    duration = models.DecimalField('Duration', decimal_places=1, max_digits=8)
    created = models.DateTimeField('Created', auto_now_add=True)
    changed = models.DateTimeField('Changed', auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('product_edit', kwargs={'pk': self.pk})

class Factory(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
