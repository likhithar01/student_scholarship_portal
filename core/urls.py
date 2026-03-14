from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # connect scholarships app
    path('', include('scholarships.urls')),
]