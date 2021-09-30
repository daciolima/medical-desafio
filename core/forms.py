from django.contrib.auth import forms

from .models import DoctorUser


class DoctorUserChangeForms(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = DoctorUser


class DoctorUserCreationForms(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = DoctorUser
