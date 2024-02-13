from django.db import models
from tinymce.models import HTMLField

class Skill(models.Model):
    title = models.CharField(max_length = 255, verbose_name = 'Навык',)
    description = models.TextField(verbose_name = 'Описание')

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self) -> str:
        return self.title


# Create your models here.
