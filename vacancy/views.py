from django.shortcuts import render
from .forms import VacancyPlacementForm
from django.contrib.auth.decorators import login_required
from utilities.decorators import company_required
from .models import Vacancy


@login_required
@company_required
def vacancy_placement(request):
    if request.method == "POST":
        print('method is POST')
        vacancy_placement_form = VacancyPlacementForm(request.POST, instance=request.user)
        if vacancy_placement_form.is_valid():
            print('form is valid')
            vacancy_placement_form.save()
    else:
        vacancy_placement_form = VacancyPlacementForm(request.POST)
    return render(request, 'vacancy_placement.html', context={
        'vacancy_placement_form': vacancy_placement_form,
    })


def all_vacancies(request):
    vacancies = Vacancy.objects.all()
    return render(request, "vacancies.html", {'vacancies': vacancies, })
