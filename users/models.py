from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    middle_name = models.CharField(max_length=50, blank=True, verbose_name='Отчество')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    city = models.CharField(max_length=50, verbose_name='Город')
    position = models.CharField(max_length=100, verbose_name='Желаемая должность')
    skills = models.TextField(verbose_name='Навыки')
    experience = models.PositiveIntegerField(default=0, verbose_name='Опыт (в годах)')
    github = models.URLField(blank=True, verbose_name='GitHub')
    linkedin = models.URLField(blank=True, verbose_name='LinkedIn')
    portfolio = models.URLField(blank=True, verbose_name='Портфолио')

    def initials(self):
        middle = f" {self.middle_name[0]}." if self.middle_name else ""
        return f"{self.last_name} {self.first_name[0]}.{middle}"
