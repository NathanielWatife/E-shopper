from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UpdateProfileForm, UpdateUserForm
from django.contrib.auth. forms import AuthenticationForm
from django.urls import reverse
from django.http import HttpResponse


# Create your views here.
# Home page
@login_required(login_url='login')
def home(request):
    return render(request, 'store/index.html')

# signup page
def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'store/register.html', {'form': form})

# login page
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)    
                # redirect tin the default page
                next_url = request.POST.get('next', reverse('home'))
                return redirect(next_url)
            else:
                return HttpResponse("Invalid  login credentials", status=401)
        else:
            return render(request, 'store/login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'store/profile.html', {'user_form': user_form, 'profile_form': profile_form})