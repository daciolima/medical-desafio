from django.contrib.auth.models import AbstractUser
from django.db import models


class Registry(models.Model):
    type = models.CharField(max_length=10, blank=False, null=False)


class DoctorUser(AbstractUser):
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



# * Nome : *CharField*
# * E-mail : *CharField*
# * Senha : *CharField*
# * Data de Criacao : *DateTimeField*