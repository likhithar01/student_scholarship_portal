from django.contrib import admin
from django.urls import path, include
from scholarships import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # HOME PAGE
    path('', views.home, name='home'),

    # SCHOLARSHIPS PAGE
    path('scholarships/', views.scholarships, name='scholarships'),
]