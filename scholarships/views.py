from django.shortcuts import render, redirect
from .models import Scholarship, Application
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


def scholarships(request):
    query = request.GET.get('q', '')
    if query:
        scholarships_list = Scholarship.objects.filter(title__icontains=query)
    else:
        scholarships_list = Scholarship.objects.all()
    return render(request, 'scholarships.html', {'scholarships': scholarships_list})


@login_required
def apply(request, id):
    scholarship = Scholarship.objects.get(id=id)

    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        marks = request.POST.get('marks')
        income = request.POST.get('income')
        document = request.FILES.get('document')

        if not all([full_name, email, marks, income, document]):
            return render(request, 'apply.html', {
                'scholarship': scholarship,
                'error': 'All fields are required.',
            })

        Application.objects.create(
            user=request.user,
            scholarship=scholarship,
            full_name=full_name,
            email=email,
            marks=int(marks),
            income=int(income),
            document=document
        )
        return redirect('dashboard')

    return render(request, 'apply.html', {'scholarship': scholarship})


@login_required
def dashboard(request):
    applications = Application.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'applications': applications})