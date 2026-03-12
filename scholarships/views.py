from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Scholarship,Application


def scholarship_list(request):

    query = request.GET.get('q')

    if query:
        scholarships = Scholarship.objects.filter(title__icontains=query)
    else:
        scholarships = Scholarship.objects.all()

    return render(request,'scholarships.html',{
        'scholarships':scholarships
    })


@login_required
def apply_scholarship(request,id):

    scholarship = Scholarship.objects.get(id=id)

    if request.method == "POST":

        document = request.FILES['document']

        Application.objects.create(
            user=request.user,
            scholarship=scholarship,
            document=document
        )

        return redirect('/dashboard/')

    return render(request,'apply.html',{
        'scholarship':scholarship
    })


def is_admin(user):
    return user.is_superuser


@user_passes_test(is_admin)
def admin_dashboard(request):

    applications = Application.objects.all()

    return render(request,'admin_dashboard.html',{
        'applications':applications
    })


@user_passes_test(is_admin)
def approve_application(request,id):

    app = Application.objects.get(id=id)
    app.status = "Approved"
    app.save()

    return redirect('/scholarships/admin-dashboard/')


@user_passes_test(is_admin)
def reject_application(request,id):

    app = Application.objects.get(id=id)
    app.status = "Rejected"
    app.save()

    return redirect('/scholarships/admin-dashboard/')