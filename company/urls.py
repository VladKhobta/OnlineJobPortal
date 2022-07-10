from django.urls import path
from .import views
from vacancy.views import vacancy_placement as vacancy_placement_view

urlpatterns = [
    path('company_register/', views.company_register, name='company_register'),
    path('profile/', views.company_profile, name='company_profile'),
    path('profile_update/', views.company_profile_update, name='company_profile_update'),
    path('vacancy_placement/', vacancy_placement_view, name='vacancy_placement'),
]
