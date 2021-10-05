from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import AppointmentTodayManager


class DoctorUser(AbstractUser):
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Patient(models.Model):
    name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=80, null=False)
    number = models.CharField(max_length=15, null=False)
    complement = models.CharField(max_length=50, null=False, blank=True)
    neighborhood = models.CharField(
        max_length=50, null=False, blank=False, default="Faltando"
    )
    zip_code = models.IntegerField()
    phone = models.CharField(max_length=16, null=False, blank=True)
    city = models.CharField(max_length=50, null=False)
    state = models.CharField(max_length=50, null=False)
    country = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "patient"
        verbose_name_plural = "patients"
        ordering = ["-id"]

    def __str__(self):
        return self.name


class Appointment(models.Model):
    STATUS_CHOICE = (
        ("not_confirme", "A Confirmar"),
        ("confirmed", "Confirmado"),
        ("done", "Finalizado"),
    )
    title = models.CharField(max_length=40, blank=False)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICE)
    doctor = models.ForeignKey(DoctorUser, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="app")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Managers
    objects = models.Manager()
    appointment_today = AppointmentTodayManager()

    class Meta:
        verbose_name = "appointment"
        verbose_name_plural = "appointments"
        ordering = ["-id"]

    def __str__(self):
        return f"{self.title} {self.status_display()}"

    def status_verbose(self):
        return dict(Appointment.STATUS_CHOICE)[self.status]
