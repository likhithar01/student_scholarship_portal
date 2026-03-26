from django.contrib import admin
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # AUTH
    path('login/', user_views.login_view, name='login'),
    path('register/', user_views.register_view, name='register'),
    path('logout/', user_views.logout_view, name='logout'),

    # APPS
    path('', include('scholarships.urls')),
]