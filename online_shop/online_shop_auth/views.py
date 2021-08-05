from django.contrib.auth import logout, get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from online_shop.online_shop_auth.forms import SignUpForm, SignInForm


UserModel = get_user_model()


class SignUpView(CreateView):
    template_name = 'profiles/sign_up.html'
    model = UserModel
    form_class = SignUpForm
    success_url = reverse_lazy('index')


class SignInView(LoginView):
    template_name = 'profiles/sign-in.html'
    form_class = SignInForm

    def get_success_url(self):
        return reverse('index')


def sign_out(request):
    logout(request)
    return redirect('index')
