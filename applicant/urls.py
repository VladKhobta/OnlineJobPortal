from django.urls import path
from .import views

urlpatterns = [
    path('applicant_register/', views.applicant_register, name='applicant_register'),
    path('profile/', views.profile, name='applicant_profile')
]
