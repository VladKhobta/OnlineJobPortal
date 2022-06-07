from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    # path('applicant_register/', views.applicant_register, name='applicant_register')
]