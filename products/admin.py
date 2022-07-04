from django.contrib import admin
from .models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','is_active','price','stock','image_preview','description')

    def image_preview(self,obj):
        return obj.image_preview

admin.site.register(Product,ProductAdmin)