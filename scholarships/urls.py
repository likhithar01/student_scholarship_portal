from django.urls import path
from . import views

urlpatterns = [

path('',views.scholarship_list),

path('apply/<int:id>/',views.apply_scholarship),

path('admin-dashboard/',views.admin_dashboard),

path('approve/<int:id>/',views.approve_application),

path('reject/<int:id>/',views.reject_application),

]