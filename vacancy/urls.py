from django.urls import path
from .import views

urlpatterns = [
    path('vacancies_searching/', views.all_vacancies, name='all_vacancies'),
]
