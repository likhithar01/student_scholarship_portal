from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Scholarship, Application
from .forms import RegisterForm

def home(request):
    scholarships = Scholarship.objects.all()[:3]
    return render(request, "home.html", {"scholarships": scholarships})


def browse_scholarships(request):
    query = request.GET.get("q")
    if query:
        scholarships = Scholarship.objects.filter(title__icontains=query)
    else:
        scholarships = Scholarship.objects.all()
    return render(request, "scholarships.html", {"scholarships": scholarships})


@login_required
def apply_scholarship(request, id):
    scholarship = Scholarship.objects.get(id=id)
    Application.objects.create(student=request.user, scholarship=scholarship)
    return redirect("dashboard")


@login_required
def dashboard(request):
    applications = Application.objects.filter(student=request.user)
    return render(request, "dashboard.html", {"applications": applications})


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()
        return redirect("login")
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user:
            login(request, user)
            return redirect("dashboard")
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("home")