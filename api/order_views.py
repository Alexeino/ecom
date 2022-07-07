from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .serializers import OrderSerializer
from orders.models import Order
from django.views.decorators.csrf import csrf_exempt
import ast
from  .utils import validate_user_session,  extract_data



@csrf_exempt
def add(request,id,token):
    if not validate_user_session(id,token):
        return JsonResponse({"error":"Please login...",'code':'1'})

    if request.method == "POST":
        data = extract_data(request)
        user_id = id
        transaction_id = data['transaction_id']
        amount = data['amount']
        products = data['products']
        
        total_products  = len(products.split(',')[:-1])
        UserModel = get_user_model()
        
        try:
            user = UserModel.objects.get(pk=id)
        except UserModel.DoesNotExist:
            return JsonResponse({"error":"User does not exist !"})

        order = Order(
            user = user,
            product_names = products,
            total_products = total_products,
            transaction_id = transaction_id,
            total_amount = amount
        )
        order.save()
        return JsonResponse({
            "success":True,
            "error":False,
            "message":"Order Placed successfully."
        })
        
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer  