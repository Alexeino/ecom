from django.urls import path,include
from .views import ProductViewSet, CategoryViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'product',ProductViewSet)
router.register(r'category',CategoryViewSet)

urlpatterns = [
    path('',include(router.urls))
]
