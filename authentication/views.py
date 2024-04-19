from .forms import *
from django.contrib import messages
from django.shortcuts import render, redirect
from homework_app.models import SubjectTeacher
from django.contrib.auth import login,logout, authenticate


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = LoginForm()
    return render(request, 'authentication/login.html', {'form': form})


def user_signup(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            group = signup_form.cleaned_data['group']
            subject = signup_form.cleaned_data['subject']
            group.user_set.add(user)
            if group.name == 'Teacher':
                print(subject, type(subject))
                SubjectTeacher.objects.create(teacher=user, subject=subject)
            return redirect('user_login')
        # else:
        #     for field, errors in signup_form.errors.items():
        #         for error in errors:
        #             messages.error(request, f"{field}: {error}")
    else:
        signup_form = SignupForm()

    return render(request, 'authentication/signup.html', {'signup_form': signup_form})


def user_logout(request):
    logout(request)
    return redirect('user_login')