from django.shortcuts import render
from .models import Scholarship

def home(request):
    scholarships = Scholarship.objects.all()[:3]
    return render(request, 'home.html', {'scholarships': scholarships})


def scholarships(request):
    query = request.GET.get('q')

    if query:
        scholarships = Scholarship.objects.filter(title__icontains=query)
    else:
        scholarships = Scholarship.objects.all()

    return render(request, 'scholarships.html', {'scholarships': scholarships})