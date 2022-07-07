from rest_framework import viewsets
from .serializers import *
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout
from django.contrib.auth.hashers import check_password
import re
from .utils import generate_session_token
from rest_framework.permissions import AllowAny    
import ast

@csrf_exempt # To exempt this post method from csrf validation
def signin(request):
    if not request.method == "POST":  # Only allowing Post requests
        return JsonResponse(
            {
                "error":"Get method not allowed!"
            }
        )
    

    data = request.body.decode("UTF-8")
    data = ast.literal_eval(data)
    username = data['email']    # Extracting username and password sent in request
    password = data['password']

# Email and Password Validation Part
    if not re.match("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$",str(username)): # Check if email is valid format using regexr
        return JsonResponse({
            "error": "Invalid Email! Enter a valid email"
        })
        
    UserModel = get_user_model() # Refrenced to current AUTH_USER_MODEL => CustomUser

    try:
        user= UserModel.objects.get(email = username) # Fetch user based on email

        if user.check_password(password) :  # Check if password matches .... if matches
            usr_dict = UserModel.objects.filter(email=username).values().first() # Fetching all values of the user not just the object
            print(usr_dict)
            usr_dict.pop('password') # Remove the password key  value pair because we don't want to send the password as response

            if user.session_token != "0": # Check if user not already logged in means session_token is there.
                user.session_token = "0"  # If already logged in then reset that session_token
                user.save()
                return JsonResponse({"error":"Previous session exists !"}) 
            # If session_token is not set 
            token = generate_session_token() # Generate random token
            user.session_token = token # update user's session token
            user.save()
            login(request,user) # Login now
            return JsonResponse( # Send that token and data as response
                {
                    'token':token,
                    'user':usr_dict
                }
            )
        else:
            # If check_password(password) returns False, means password is incorrect
            return JsonResponse({"error":"Wrong Password !"})

    except UserModel.DoesNotExist:
        return JsonResponse({"error":"Invalid credentials!"})
    
def signout(request,id):
    logout(request)
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        user.session_token = "0"
        user.save()
    except UserModel.DoesNotExist:
        return JsonResponse({"error":"Invalid user ID"})
    
    return JsonResponse({"success":"Succesfully Logged out !"})

class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {
        'create':[AllowAny]
    }
    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializer

    def get_permission(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]