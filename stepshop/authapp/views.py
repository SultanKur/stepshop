from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm


def login(request):
    title = "вход"

    login_form = ShopUserLoginForm(data=request.POST)

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))

    context = {
        'title': title,
        'login_form': login_form,
    }
    return render(request, 'auth/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

def reqister(request):
    title = 'регистрация'

    if request.method == "POST":
        reqister_form = ShopUserRegisterForm(request.POST, request.FILES)

        if reqister_form.is_valid():
            reqister_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
        else:
            reqister_form = ShopUserRegisterForm()


