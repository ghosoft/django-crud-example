# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import Product
from .forms import ProductForm

class ProductList(ListView): 
    paginate_by = 10
    model = Product
    def get_queryset(self, *args, **kwargs):
        qs = super(ProductList, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("id")
        return qs

class ProductDetail(DetailView): 
    model = Product

class ProductCreate(SuccessMessageMixin, CreateView): 
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    success_message = "Experiment successfully created!"

class ProductUpdate(SuccessMessageMixin, UpdateView): 
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    success_message = "Experiment successfully updated!"

class ProductDelete(SuccessMessageMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')
    success_message = "Experiment successfully deleted!"


