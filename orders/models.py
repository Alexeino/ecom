from django.db import models
from users.models import CustomUser
from products.models import Product
# Create your models here.
class OrderItem(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return "{} - {} ".format(self.user.name,self.product.name)

class Order(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shiping_address = models.TextField()
    order_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return "{self.user.name} + Order"
    
