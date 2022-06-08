from django.shortcuts import render, redirect
from .forms import RecruiterSignUpForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def recruiter_register(request):
    if request.method == 'POST':
        form = RecruiterSignUpForm(request.POST)
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
        form = RecruiterSignUpForm
    return render(request, 'recruiter_register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'recruiter_profile.html')
