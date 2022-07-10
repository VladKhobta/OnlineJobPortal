from django.shortcuts import render, redirect
from .forms import CompanySignUpForm, CompanyProfileForm, CompanyUpdateForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from account.forms import UserProfileForm, UserUpdateForm

# Create your views here.


def company_register(request):
    if request.method == 'POST':
        form = CompanySignUpForm(request.POST)
        print('1')
        if form.is_valid():
            print('2')
            form.save()
            cd = form.cleaned_data
            email = cd.get('email')
            password = cd.get('password1')
            user = authenticate(email=email, password=password)
            print(user.usertype.type)
            login(request, user)
            return redirect('/')
        else:
            print('3')
    else:
        form = CompanySignUpForm
    return render(request, 'company_register.html', {'form': form})


@login_required
def company_profile(request):
    user_form = UserProfileForm(instance=request.user)
    company_form = CompanyProfileForm(instance=request.user.company)
    return render(request, 'company_profile.html', context={
        'user': request.user,
        'user_form': user_form,
        'company_form': company_form,
    })


@login_required
def company_profile_update(request):
    print('there')
    if request.method == 'POST':
        print('Got it')
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        company_update_form = CompanyUpdateForm(request.POST, instance=request.user.company)
        if user_update_form.is_valid() and company_update_form.is_valid():
            print('forms are valid')
            company_update_form.save()
            return redirect('profile')
        else:
            print('false')
    else:
        user_update_form = UserUpdateForm
        company_update_form = CompanyUpdateForm
    return render(request, 'company_profile_update.html', context={
        'user': request.user,
        'user_update_form': user_update_form,
        'company_update_form': company_update_form,
    })
