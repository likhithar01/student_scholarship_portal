from django.contrib import admin
from django.urls import path
from scholarships import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('apply/<int:id>/', views.apply, name='apply'),
    path('dashboard/', views.dashboard, name='dashboard'),
]