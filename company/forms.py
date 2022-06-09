from django.contrib.auth.forms import UserCreationForm
from django import forms
from account.models import User, UserType
from .models import Company
from django.db import transaction


class CompanySignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    phone_number = forms.CharField(max_length=20,
                                   required=True,
                                   error_messages={
                                       'required': 'Phone number can not be blank',
                                   },
                                   )

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
        user.email = self.cleaned_data.get('email')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.save()
        UserType.objects.create(user=user)
        user.usertype.type = 'COMPANY'
        user.usertype.save()
        company = Company.objects.create(user=user)
        company.save()
        return user


class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'designation',
        ]
