from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from .forms import LoginForm
from django.contrib.auth import authenticate, login


class HomeView(View):
    def get(self, request):
        return render(request, 'core/index.html')


class UmlView(View):
    def get(self, request):
        return render(request, 'core/uml.html')


class LoginView(View):
    def get(self, request):
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
                        return render(request, 'core/index.html')
                    else:
                        return HttpResponse('Usuario desabilitado')
                else:
                    return HttpResponse('preenchimento inválido')
        else:
            form = LoginForm()
        return render(request, 'core/login.html', {'form': form})








