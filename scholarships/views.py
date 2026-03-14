from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def scholarships(request):
    return render(request, 'scholarships.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def login_view(request):
    return render(request, 'login.html')


def register_view(request):
    return render(request, 'register.html')