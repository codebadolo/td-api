from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)

        if user:
            login(request, user)
            return Response({'message': 'Login successful', 'user': user.email})
        return Response({'error': 'Invalid credentials'}, status=401)


@csrf_exempt
def user_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.create_user(email=email, password=password)
            return JsonResponse({'message': 'Signup successful', 'user': user.email})
        except IntegrityError:
            return JsonResponse({'error': 'Email already exists'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'Logout successful'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def user_profile(request):
    if request.user.is_authenticated:
        return JsonResponse({'email': request.user.email, 'bio': request.user.bio})
    return JsonResponse({'error': 'User not authenticated'}, status=401)
