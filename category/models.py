from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"

    def __str__(self):
        return self.name
    