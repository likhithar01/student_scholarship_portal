from django.shortcuts import render, redirect
from .models import Scholarship, Application
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


def home(request):
    query = request.GET.get('q')
    scholarships = Scholarship.objects.all()

    if query:
        scholarships = scholarships.filter(title__icontains=query)

    return render(request, 'home.html', {'scholarships': scholarships})


@login_required
def apply(request, id):
    scholarship = Scholarship.objects.get(id=id)

    if request.method == 'POST':
        marks = int(request.POST['marks'])
        income = int(request.POST['income'])

        # Eligibility check
        eligible = marks >= scholarship.min_marks and income <= scholarship.max_income

        if not eligible:
            return render(request, 'apply.html', {
                'scholarship': scholarship,
                'error': 'You are not eligible for this scholarship'
            })

        Application.objects.create(
            user=request.user,
            scholarship=scholarship,
            full_name=request.POST['full_name'],
            email=request.POST['email'],
            marks=marks,
            income=income,
            document=request.FILES['document']
        )

        # Email (console for now)
        send_mail(
            'Application Submitted',
            'Your scholarship application was submitted successfully.',
            'from@example.com',
            [request.POST['email']],
            fail_silently=True,
        )

        return redirect('dashboard')

    return render(request, 'apply.html', {'scholarship': scholarship})


@login_required
def dashboard(request):
    applications = Application.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'applications': applications})