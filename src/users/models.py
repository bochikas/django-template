from django.contrib.auth.models import AbstractUser
from django.db import models

from base.models import UpdatedAtModel


class User(UpdatedAtModel, AbstractUser):
    """Пользователь."""

    short_name = models.CharField(verbose_name="Краткое имя", max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.username})"
