from django.db import models
from tinymce.models import HTMLField


class Article(models.Model):
    title = models.CharField(max_length = 255, verbose_name = 'Новость')
    description = HTMLField(verbose_name = 'Описание')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


    def __str__(self) -> str:
        return self.title




# Create your models here.
