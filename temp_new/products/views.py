from django.shortcuts import render
from django.views.generic import TemplateView

app_name = 'products'


# Create your views here.
class ProductsListView(TemplateView):
    template_name = 'products/products-list.html'
