from django.urls import path
from .import views

urlpatterns = [
    path('company_register/', views.company_register, name='company_register'),
    path('profile/', views.company_profile, name='company_profile')
]
