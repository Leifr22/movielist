from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from movielist import settings
from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'user/login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterView(CreateView):
    form_class = RegisterUserForm
    template_name = 'user/register.html'
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('login')


def register(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'user/register_done.html')
        else:
            form = RegisterUserForm()
    return render(request, 'user/register.html', {'form': form})


class ProfileUser(UpdateView):
    model=get_user_model()
    form_class = ProfileUserForm
    template_name = 'user/profile.html'
    success_url = reverse_lazy("profile_changed.html")
    extra_context = {'title': 'Профиль пользователя'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['default_image'] = settings.DEFAULT_USER_IMAGE
        return context

    def get_success_url(self):
        return reverse_lazy('profile')
    def get_object(self, queryset=None):
        return self.request.user
class UserPasswordChange(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("user/password_change_done")
    template_name = "user/password_change_form.html"
