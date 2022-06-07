from django.urls import path
from .import views

urlpatterns = [
    # path('register/', ),
    path('applicant_register/', views.applicant_register, name='applicant_register'),

]