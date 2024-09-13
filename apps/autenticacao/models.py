from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    username = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(unique=True)
    EMAIL_FIELD = email
    USERNAME_FIELD = username

    def __str__(self) -> str:
        return self.email