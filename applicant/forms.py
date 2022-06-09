from django.contrib.auth.forms import UserCreationForm
from django import forms
from account.models import User, UserType
from .models import Applicant
from django.db import transaction


class ApplicantSignUpForm(UserCreationForm):
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
        user_type = UserType.objects.create(user=user)
        user_type.type = 'APPLICANT'
        user.usertype.save()
        applicant = Applicant.objects.create(user=user)
        applicant.save()
        return user
