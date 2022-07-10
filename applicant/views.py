from django.shortcuts import render, redirect
from .forms import ApplicantSignUpForm, ApplicantProfileForm, ApplicantUpdateForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from account.forms import UserProfileForm, UserUpdateForm

# Create your views here.


def applicant_register(request):
    if request.method == 'POST':
        form = ApplicantSignUpForm(request.POST)
        print('1')
        if form.is_valid():
            print('2')
            form.save()
            cd = form.cleaned_data
            email = cd.get('email')
            password = cd.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('/')
        else:
            print('3')
    else:
        form = ApplicantSignUpForm
    return render(request, 'applicant_register.html', {'form': form})


@login_required
def applicant_profile(request):
    user_form = UserProfileForm(instance=request.user)
    applicant_form = ApplicantProfileForm(instance=request.user.applicant)
    return render(request, 'applicant_profile.html', context={
        'user': request.user,
        'user_form': user_form,
        'applicant_form': applicant_form,
    })


@login_required
def applicant_profile_update(request):
    print('there')
    if request.method == 'POST':
        print('Got it')
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        applicant_update_form = ApplicantUpdateForm(request.POST, instance=request.user.applicant)
        if user_update_form.is_valid() and applicant_update_form.is_valid():
            print('forms are valid')
            applicant_update_form.save()
            return redirect('profile')
        else:
            print('false')
    else:
        user_update_form = UserUpdateForm
        applicant_update_form = ApplicantUpdateForm
    return render(request, 'applicant_profile_update.html', context={
        'user': request.user,
        'user_update_form': user_update_form,
        'applicant_update_form': applicant_update_form,
    })
