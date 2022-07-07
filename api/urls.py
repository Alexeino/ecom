from django.urls import path,include

from .order_views import OrderViewSet, add
from .user_views import UserViewSet , signin, signout
from .category_views import CategoryViewSet
from .product_views import ProductViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'product',ProductViewSet)
router.register(r'category',CategoryViewSet)
router.register(r'user',UserViewSet)
router.register(r'order',OrderViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('login/', signin,name="signin"),
    path('logout/<int:id>', signout,name="signout"),
    path('add/<str:id>/<str:token>/',add,name="order.add")
]
