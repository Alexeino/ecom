from django.shortcuts import render
from rest_framework import viewsets
from products.models import Product
from category.models import Category
from .serializers import *

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    """
    Viewset for Product Model
    """
    queryset= Product.objects.all().order_by('name')
    serializer_class = ProductSerializer
    
class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer