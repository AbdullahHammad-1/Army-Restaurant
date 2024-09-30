from django.contrib import messages
from django.shortcuts import render, redirect
from users.forms import RegisterForm, ProfileForm
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.views.generic import UpdateView

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


class EditProfileView(UpdateView):
    model = Profile
    form_class = ProfileForm
    login_required = True
    template_name = 'edit_profile.html'
    success_url = '/users/profile/'  # Redirect after a successful update

    def get_object(self):
        return self.request.user.profile  # Get the profile of the logged-in user

