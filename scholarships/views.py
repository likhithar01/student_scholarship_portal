from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Scholarship, Application


def scholarship_list(request):

    search = request.GET.get('search')

    if search:
        scholarships = Scholarship.objects.filter(title__icontains=search)
    else:
        scholarships = Scholarship.objects.all()

    paginator = Paginator(scholarships, 6)
    page = request.GET.get('page')
    scholarships = paginator.get_page(page)

    return render(request, 'scholarships/list.html', {'scholarships': scholarships})


@login_required
def apply_scholarship(request, id):

    scholarship = get_object_or_404(Scholarship, id=id)

    Application.objects.create(
        user=request.user,
        scholarship=scholarship
    )

    return redirect('dashboard')


@login_required
def dashboard(request):

    applications = Application.objects.filter(user=request.user)

    return render(request, 'dashboard.html', {
        'applications': applications
    })