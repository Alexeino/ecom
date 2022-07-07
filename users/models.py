from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self,name,email,password,**other_fields):
        if not email:
            raise ValueError("You must provide an email address!")
        
        email = self.normalize_email(email)
        user = self.model(email = email,name=name,**other_fields)
        user.set_password(password)

        user.save()

        return user

    def create_superuser(self,name,email,password,**other_fields):
        other_fields.setdefault("is_staff",True)
        other_fields.setdefault("is_active",True)
        other_fields.setdefault("is_superuser",True)

        if other_fields.get('is_staff') is not True:
            raise ValueError("Superuser must be assigned to is_staff = True")
        if other_fields.get('is_active') is not True:
            raise ValueError("Superuser must be assigned to is_active = True")
        if other_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must be assigned to is_active = True")
        return self.create_user(name,email,password,**other_fields)

# Create your models here.
class CustomUser(AbstractBaseUser):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.TextField()
    gender = models.CharField(max_length=50)
    email = models.EmailField(max_length=254,unique=True)
    is_staff = models.BooleanField(default= False)
    is_active = models.BooleanField(default = True)
    is_superuser = models.BooleanField(default = False)

    session_token = models.CharField(max_length=10,default=0,null=True,blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name','phone']

    objects = UserManager()

    def __str__(self):
        return self.name

    def has_module_perms(self,app_label):
        return self.is_superuser
    
    def has_perm(self,perm,obj=None):
        return self.is_superuser