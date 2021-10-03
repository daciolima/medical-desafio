from django.contrib.auth import forms
from django import forms as form_login

# from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker

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


# STATUS = (
#     ('', 'Selecione...'),
#     ('not_confirme', 'A Confirmar'),
#     ('confirmed', 'Confirmado'),
#     ('done', 'Finalizando')
# )


# class AppointmentForm(form_login.Form):
# title = form_login.CharField()
# date = form_login.DateField()
# time = form_login.CharField()
# description = form_login.TimeField()
# status = form_login.ChoiceField(choices=STATUS)
# doctor = form_login.ModelChoiceField(queryset=DoctorUser.objects.all())
# patient = form_login.ModelChoiceField(queryset=Patient.objects.all())


class AppointmentForm(form_login.ModelForm):
    class Meta:
        model = Appointment
        exclude = "update_at", "created_at"

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({"class": "form-control"})
        self.fields["date"].widget.attrs.update(
            {
                "class": "form-control datetimepicker-input",
                "id": "datetimepicker1",
                "data - target": "#datetimepicker1",
            }
        )
        self.fields["time"].widget.attrs.update(
            {
                "class": "form-control col-sm-4",
                "id": "id_time",
                "data-autoclose": "true",
                "data-placement": "right",
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
