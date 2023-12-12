from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as auth_logout
from main.models import User 
import json

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login sukses!"
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)

@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)
    
@csrf_exempt
def register(request):
    if request.method != "POST":
        return JsonResponse({
            "status": False,
            "message": "Invalid request method."
        }, status=405)

    print("Request Body:", request.body) 

    if not request.body:
        return JsonResponse({
            "status": False,
            "message": "Empty request body."
        }, status=400)

    try:
        data = json.loads(request.body.decode('utf-8'))

        username = data.get('username')
        password = data.get('password')
        is_customer = data.get('is_customer', False) 
        is_employee = data.get('is_employee', False) 

        if not username or not password:
            return JsonResponse({
                "status": False,
                "message": "Username and password are required."
            }, status=400)

        new_user = User.objects.create_user(
        username=username,
        password=password, 
        is_customer=is_customer,
        is_employee=is_employee
    )
        return JsonResponse({
            "status": True,
            "message": "Account created successfully!",
            "user_id": new_user.id,
        }, status=201)

    except json.JSONDecodeError as e:
        return JsonResponse({
            "status": False,
            "message": "Invalid JSON format: " + str(e)
        }, status=400)
    except Exception as e:
        return JsonResponse({
            "status": False,
            "message": "An error occurred: " + str(e)
        }, status=500)
