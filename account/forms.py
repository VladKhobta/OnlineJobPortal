from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from account.models import User, UserType


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'email',
            'password',
        ]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'phone_number',
        ]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
        ]
