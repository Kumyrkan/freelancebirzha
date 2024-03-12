from django.db import models
from tinymce.models import HTMLField

class Faq(models.Model):
    title = models.CharField(max_length = 255, verbose_name = 'Часто задаваемый вопрос')
    description = HTMLField(verbose_name = 'Описание')

    class Meta:
        verbose_name = 'Часто задаваемый вопрос'
        verbose_name_plural = 'Часто задаваемые вопросы'

    def __str__(self) -> str:
        return self.title


# Create your models here.
