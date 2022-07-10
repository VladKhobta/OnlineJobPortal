from django import forms
from vacancy.models import Vacancy
from django.db import transaction


class VacancyPlacementForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = [
            'title',
            'required_experience',
            'salary',
            'description',
        ]

    @transaction.atomic
    def save(self):
        print('Save)')
        user = super().save(commit=False)
        print(user)
        vacancy = Vacancy.objects.create(company=user.company)
        cd = self.cleaned_data
        vacancy.title = cd.get('title')
        vacancy.required_experience = cd.get('required_experience')
        vacancy.salary = cd.get('salary')
        vacancy.description = cd.get('description')
        vacancy.save()
        return vacancy

