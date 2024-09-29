from django.contrib import messages
from django.shortcuts import render, redirect
from users.forms import RegisterForm
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            message = messages.success(request, f'Welcome {username}, your account is created successfully.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)

    return render(request, 'logout.html')


def login_view(request):
    login(request)

    return render(request, 'login.html')


@login_required
def profile(request):
    return render(request, 'profile.html')

