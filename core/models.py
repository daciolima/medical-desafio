from django.contrib.auth.models import AbstractUser
from django.db import models


class DoctorUser(AbstractUser):
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Patient(models.Model):
    name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=80, null=False)
    number = models.IntegerField()
    complement = models.CharField(max_length=50, null=False, blank=True)
    neighborhood = models.CharField(
        max_length=50, null=False, blank=False, default="Faltando"
    )
    zip_code = models.IntegerField()
    phone = models.IntegerField()
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


STATUS_CHOICE = (
    ("not_confirme", "A Confirmar"),
    ("confirmed", "Confirmado"),
    ("done", "Finalizado"),
)


class Appointment(models.Model):
    title = models.CharField(max_length=40, blank=False)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICE)
    doctor = models.ForeignKey(DoctorUser, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="app")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "appointment"
        verbose_name_plural = "appointments"
        ordering = ["-id"]

    def __str__(self):
        return self.title
