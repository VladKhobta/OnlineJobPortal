from django.urls import path
from .import views

urlpatterns = [
    path('recruiter_register/', views.recruiter_register, name='recruiter_register'),
    path('profile/', views.profile, name='recruiter_profile')
]