from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("scholarships/", views.browse_scholarships, name="scholarships"),
    path("apply/<int:id>/", views.apply_scholarship, name="apply"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]