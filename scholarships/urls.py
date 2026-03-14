from django.urls import path
from . import views

urlpatterns = [

    # HOME PAGE
    path('', views.home, name='home'),

    # BROWSE SCHOLARSHIPS
    path('scholarships/', views.scholarships, name='scholarships'),

    # LOGIN
    path('login/', views.login_view, name='login'),

    # REGISTER
    path('register/', views.register_view, name='register'),

    # DASHBOARD
    path('dashboard/', views.dashboard, name='dashboard'),

]
