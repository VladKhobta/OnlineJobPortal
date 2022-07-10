from django.urls import path
from .import views

urlpatterns = [
    path('applicant_register/', views.applicant_register, name='applicant_register'),
    path('profile/', views.applicant_profile, name='applicant_profile'),
    path('profile_update/', views.applicant_profile_update, name='applicant_profile_update'),
]
