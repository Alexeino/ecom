from django.db import models
from category.models import Category
from django.utils.html import mark_safe
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='products',null=True,blank=True)
    is_active = models.BooleanField(default=True)
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True,blank=True)

    @property
    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))
        return ""

    def __str__(self):
        return self.name
    