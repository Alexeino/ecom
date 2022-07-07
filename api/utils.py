import random
from django.contrib.auth import get_user_model
import ast

def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice(
        [chr(i) for i in range(97,123)] +
        [str(i) for i in range(10)]
        ) for _ in range(length))
    
def validate_user_session(id,token):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False
    

def extract_data(request):
    data = request.body.decode("UTF-8")
    data = ast.literal_eval(data)
    
    return  data