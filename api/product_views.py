from django.shortcuts import render
from rest_framework import viewsets
from products.models import Product
from category.models import Category
from users.models import CustomUser
from .serializers import *
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout
from django.contrib.auth.hashers import check_password
import re


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    """
    Viewset for Product Model
    """
    queryset= Product.objects.all().order_by('name')
    serializer_class = ProductSerializer