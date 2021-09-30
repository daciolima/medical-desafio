from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import DetailView, ListView


class HomeView(View):
    def get(self, request):
        return render(request, 'core/index.html')


class UmlView(View):
    def get(self, request):
        return render(request, 'core/uml.html')


class Login(View):
    def get(self, request):
        return render(request, 'core/login.html')







