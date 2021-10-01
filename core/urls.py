from django.urls import path

from .views import IndexView, UmlView, LoginView, LogoutView, ListPatientView

app_name = "core"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('projeto', UmlView.as_view(), name="uml"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('list/', ListPatientView.as_view(), name="patient")
]