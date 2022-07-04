from django.contrib import admin
from .models import CustomUser

class UserAdmin(admin.ModelAdmin):
    exclude= ('is_superuser','last_login')

# Register your models here.
admin.site.register(CustomUser,UserAdmin)