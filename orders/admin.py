from django.contrib import admin
from .models import Order,OrderItem
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','get_products',
                    'created_at','order_confirmed')

    def get_products(self,obj):
        return ",".join(p.product.name for p in obj.items.all())

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('user','product','quantity')

admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)