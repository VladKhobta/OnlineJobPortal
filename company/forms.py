from django.contrib.auth.forms import UserCreationForm
from django import forms
from account.models import User, UserType
from .models import Company
from django.db import transaction
from utilities.validators import validate_interval


class CompanySignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    phone_number = forms.CharField(max_length=20,
                                   required=True,
                                   error_messages={
                                       'required': 'Phone number can not be blank',
                                   },
                                   )
    designation = forms.CharField(max_length=254, required=True)

    class Meta:
        model = User
        fields = [
            'email',
            'phone_number',
            'password1',
            'password2',
        ]

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        cd = self.cleaned_data
        user.email = cd.get('email')
        user.phone_number = cd.get('phone_number')
        user.save()
        UserType.objects.create(user=user)
        user.usertype.type = 'COMPANY'
        user.usertype.save()
        company = Company.objects.create(user=user)
        company.designation = cd.get('designation')
        company.save()
        return user


class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'designation',
            'establishment_date',
            'description',
        ]


class CompanyUpdateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'designation',
            'establishment_date',
            'description',
        ]

    # @transaction.atomic
    # def save(self):
    #     company = super().save(commit=False)
    #     cd = self.cleaned_data
    #     company.designation = cd.get('designation')
    #     company.establishment_date = cd.get('establishment_date')
    #     company.description = cd.get('description')
    #     company.save()
    #     return company
