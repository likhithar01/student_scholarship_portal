from django.shortcuts import render, redirect
from .models import Scholarship, Application
from django.contrib.auth.decorators import login_required


def scholarships(request):
    data = Scholarship.objects.all()
    return render(request, 'scholarships.html', {'scholarships': data})


@login_required
def apply(request, id):
    scholarship = Scholarship.objects.get(id=id)

    if request.method == "POST":
        marks = int(request.POST.get('marks'))
        income = int(request.POST.get('income'))

        Application.objects.create(
            user=request.user,
            scholarship=scholarship,
            marks=marks,
            income=income
        )

        return redirect('dashboard')

    return render(request, 'apply.html', {'scholarship': scholarship})


@login_required
def dashboard(request):
    apps = Application.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'applications': apps})


def internships(request):
    data = Scholarship.objects.filter(category="Internship")
    return render(request, 'internships.html', {'internships': data})