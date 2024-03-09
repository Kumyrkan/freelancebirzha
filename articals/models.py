from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

class Category(models.Model):
    title = models.CharField('Наименование категории', max_length = 255)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('pk',)

    def __str__(self) -> str:
        return self.title

class Article(models.Model):
    title = models.CharField(max_length = 255, verbose_name = 'Заголовок')
    description = HTMLField(verbose_name = 'Описание')
    image = models.ImageField(verbose_name = 'Изображение', null = True, blank = True)
    category = models.ForeignKey(Category, verbose_name = 'Категория', null = True, blank = True, on_delete = models.CASCADE)
    created_at = models.DateTimeField(verbose_name = 'Дата создания', default = timezone.now)
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


    def __str__(self) -> str:
        return self.title




# Create your models here.
