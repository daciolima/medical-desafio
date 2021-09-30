from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, ListView
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'core/index.html')


class UmlView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'core/uml.html')


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('core:index')
        form = LoginForm()
        return render(request, 'core/login.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(request,
                                    username=cd['username'],
                                    password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('core:index')
                    else:
                        return HttpResponse('Usuario desabilitado')
                else:
                    return HttpResponse('preenchimento inválido')
        else:
            form = LoginForm()
        return render(request, 'core/login.html', {'form': form})


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('login')





