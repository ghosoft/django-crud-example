# -*- coding: utf-8 -*-
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['description'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['start_time'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['duration'].widget.attrs = {
            'class': 'form-control col-md-6',
            'step': 'any',
            'min': '1',
        }
        self.fields['count'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['department'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['person'].widget.attrs = {
            'class': 'form-control col-md-6'
        }

    class Meta:
        model = Product
        fields = ('name', 'description', 'start_time', 'duration', 'count', 'department', 'person')