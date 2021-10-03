from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import DoctorUser, Patient, Appointment

from .forms import DoctorUserCreationForms, DoctorUserChangeForms


@admin.register(DoctorUser)
class DoctorUserAdmin(UserAdmin):
    form = DoctorUserChangeForms
    add_form = DoctorUserCreationForms
    model = DoctorUser
    fieldsets = UserAdmin.fieldsets + (("Campos Personalizados", {"fields": ("bio",)}),)


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone",
    )


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "title",
        "status",
    )
