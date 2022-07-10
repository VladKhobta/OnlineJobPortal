from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import LoginForm


def register_view(request):
    return render(request, '../templates/register.html')


def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):
    form = LoginForm(data=request.POST)
    if request.method == 'POST':
        print(1)
        if form.is_valid():
            print(2)
            cd = form.cleaned_data
            email = cd.get('email')
            password = cd.get('password')
            user = authenticate(email=email, password=password)
            print(email, password)
            if user is not None:
                print(3)
                print(user.usertype.type == 'APPLICANT')
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid email or password')
        else:
            messages.error(request, 'form is invalid')
    return render(request, 'login.html', {'form': form})


@login_required
def profile(request):
    if request.user.usertype.type == 'APPLICANT':
        print('in profile view by applicant')
        return redirect('applicant_profile')
    elif request.user.usertype.type == 'COMPANY':
        print('in profile view by company')
        return redirect('company_profile')


@login_required
def profile_update(request):
    if request.user.usertype.type == 'APPLICANT':
        print('in profile edit view by applicant')
        return redirect('applicant_profile_update')
    elif request.user.usertype.type == 'COMPANY':
        print('in profile edit view by company')
        return redirect('company_profile_update')
