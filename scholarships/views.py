from django.shortcuts import render, redirect
from .models import Scholarship, Application
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .ai_model import check_eligibility   # ✅ AI IMPORT


# ✅ HOME PAGE
def home(request):
    query = request.GET.get('q')
    category = request.GET.get('category')

    scholarships = Scholarship.objects.all()

    if query:
        scholarships = scholarships.filter(title__icontains=query)

    if category:
        scholarships = scholarships.filter(category=category)

    return render(request, 'home.html', {
        'scholarships': scholarships
    })

# ✅ SCHOLARSHIPS LIST PAGE
def scholarships(request):
    query = request.GET.get('q', '')

    if query:
        scholarships_list = Scholarship.objects.filter(title__icontains=query)
    else:
        scholarships_list = Scholarship.objects.all()

    return render(request, 'scholarships.html', {'scholarships': scholarships_list})


# ✅ APPLY FUNCTION WITH AI 🔥
@login_required
def apply(request, id):
    scholarship = Scholarship.objects.get(id=id)

    if request.method == "POST":
        # 👉 Get form data
        marks = int(request.POST.get('marks'))
        income = int(request.POST.get('income'))

        # 🔥 AI CHECK
        result = check_eligibility(marks, income)

        if result == "Not Eligible":
            return render(request, 'apply.html', {
                'scholarship': scholarship,
                'error': 'AI says you are not eligible'
            })

        # ✅ SAVE APPLICATION
        Application.objects.create(
            user=request.user,
            scholarship=scholarship,
            marks=marks,
            income=income
        )

        # (optional email)
        send_mail(
            'Application Submitted',
            'Your scholarship application was submitted successfully.',
            'from@example.com',
            [request.user.email],
            fail_silently=True,
        )

        return redirect('dashboard')

    return render(request, 'apply.html', {'scholarship': scholarship})


# ✅ DASHBOARD
@login_required
def dashboard(request):
    applications = Application.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'applications': applications})

def internships(request):
    from .models import Scholarship
    internships = Scholarship.objects.filter(category="Internship")
    return render(request, 'internships.html', {'internships': internships})