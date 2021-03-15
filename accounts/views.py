import json

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect

from .forms import RegistrationForm


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(request.POST.get('password'))
            form.save()
            return JsonResponse({"status": True, "message": "Registration confirm"})
            
        else:
            errors = []
            for field in form:
                for error in field.errors:
                    errors.append(error)
            return JsonResponse({"status": False, "errors": errors})
    else:
        return JsonResponse({"message": "denied"})


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
            return JsonResponse({"status": True, "message": "User logged in"})
        else:
            return JsonResponse({"status": False, "errors": "User doesn't exist"})
    else:
        return JsonResponse({"message": "denied"})


def logout_user(request):
    logout(request)
    return redirect('core:home')
