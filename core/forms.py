from django.contrib.auth import forms
from django import forms as form_login
from .models import DoctorUser, Patient, Appointment


class DoctorUserChangeForms(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = DoctorUser


class DoctorUserCreationForms(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = DoctorUser


class LoginForm(form_login.Form):
    username = form_login.CharField(
        label="Usuário",
        widget=form_login.TextInput(attrs={"class": "form-control", "placeholder": ""}),
    )
    password = form_login.CharField(
        label="Senha",
        widget=form_login.PasswordInput(
            attrs={"class": "form-control", "placeholder": ""}
        ),
    )


class PatientForm(form_login.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"


class AppointmentForm(form_login.ModelForm):
    date = form_login.DateField(error_messages={"invalid": "Data inválida"})
    time = form_login.CharField(error_messages={"invalid": "Hora inválida"})

    class Meta:
        model = Appointment
        exclude = "update_at", "created_at"

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update(
            {
                "class": "form-control",
                "minlength": "5",
                "pattern": "^[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ ]+$",
                "title": "Mínimo 5 caracteres e apenas letras",
            }
        )
        self.fields["date"].widget.attrs.update(
            {"class": "form-control", "id": "id_date", "value": "00/00/0000"}
        )

        self.fields["time"].widget.attrs.update(
            {
                "class": "form-control col-sm-4",
                "id": "id_time",
                "data-autoclose": "true",
                "data-placement": "right",
                "value": "00:00",
                "pattern": "[0-9:]+",
                "title": "Use o Relógio para preencher o campo. Formato 00:00",
            }
        )
        self.fields["doctor"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )
        self.fields["patient"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )
        self.fields["description"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )
        self.fields["status"].widget.attrs.update(
            {
                "class": "form-control col-sm-4",
            }
        )
