from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import DoctorUser, Registry

from .forms import DoctorUserCreationForms, DoctorUserChangeForms


@admin.register(Registry)
class RegistryAdmin(admin.ModelAdmin):
    list_display = ('type',)


@admin.register(DoctorUser)
class DoctorUserAdmin(UserAdmin):
    form = DoctorUserChangeForms
    add_form = DoctorUserCreationForms
    model = DoctorUser
    fieldsets = UserAdmin.fieldsets + (
        ("Campos Personalizados", {"fields": ('bio',)}),
    )
