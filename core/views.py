from django.shortcuts import render


def index(reques):
    return render(reques, 'core/index.html')



