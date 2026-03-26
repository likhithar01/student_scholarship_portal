from django.urls import path
from . import views

urlpatterns = [
    path('', views.scholarships, name='scholarships'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('apply/<int:id>/', views.apply, name='apply'),
    path('internships/', views.internships, name='internships'),
]