from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apply/<int:id>/', views.apply, name='apply'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('internships/', views.internships, name='internships'),
]