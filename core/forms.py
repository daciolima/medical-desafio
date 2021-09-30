from django.contrib.auth import forms
from django import forms as form_login

from .models import DoctorUser


class DoctorUserChangeForms(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = DoctorUser


class DoctorUserCreationForms(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = DoctorUser


class LoginForm(form_login.Form):
    username = form_login.CharField(label='Usuário')
    password = form_login.CharField(label='Senha', widget=form_login.PasswordInput)
