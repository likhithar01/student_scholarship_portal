from django.urls import path
from . import views

urlpatterns = [

    path('', views.scholarship_list, name='scholarships'),

    path('apply/<int:id>/', views.apply_scholarship, name='apply'),

    path('dashboard/', views.dashboard, name='dashboard'),

]