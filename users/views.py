from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from scholarships.models import Scholarship, Application


def home(request):

    scholarships = Scholarship.objects.all()[:6]

    return render(request, 'home.html', {
        'scholarships': scholarships
    })


def register(request):

    if request.method == "POST":

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('/login/')

    return render(request, 'register.html')


def user_login(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect('/dashboard/')

    return render(request, 'login.html')


def user_logout(request):

    logout(request)
    return redirect('/')


@login_required
def dashboard(request):

    applications = Application.objects.filter(user=request.user)

    return render(request, 'dashboard.html', {
        'applications': applications
    })