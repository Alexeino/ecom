from rest_framework import serializers
from products.models import Product
from category.models import Category

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name','description','price'
        ,'image','stock','category')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name','description','is_active')