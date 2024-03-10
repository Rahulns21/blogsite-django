from django.contrib.auth import get_user_model, authenticate, login, logout
from .forms import *
from .decorators import *
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@user_not_authenticated
def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    CustomUser = get_user_model()  # Get the custom user model

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Check if username already exists
            username = form.cleaned_data['username']
            if CustomUser.objects.filter(username=username).exists():
                error_message = "Username already exists. Please choose a different one."
                return render(request, 'registration/register.html', {'form': form, 'error_message': error_message})
            else:
                user = form.save()
                login(request, user)
                messages.success(
                    request, f"New account created: {user.username}")
                return redirect('/')
        else:
            messages.error(request, "Fix the errors")
    else:
        form = UserRegistrationForm()

    context = {"form": form}
    return render(request, template_name='users/register.html', context=context)

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, "Logged out successfully!")
    return redirect('myapp:homepage')

@user_not_authenticated
def login_view(request):
    if request.user.is_authenticated:
        return redirect('users:homepage')

    if request.method == 'POST':
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect('myapp:homepage')

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue
                messages.error(request, error)  

    form = UserLoginForm() 
    context = {'form': form}
    return render(request=request, template_name="users/login.html", context=context)

@login_required
def profile(request, username):
    if request.method == 'POST':
        user = request.user
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()

            messages.success(request, f'{user_form}, Your profile has been updated!')
            return redirect('users:profile', user_form.username)

        for error in list(form.errors.values()):
            messages.error(request, error)

    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateForm(instance=user)
        form.fields['description'].widget.attrs = {'rows': 1}
        return render(request, 'users/profile.html', context={'form': form})

    return redirect("homepage")