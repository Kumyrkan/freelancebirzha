from django.db import models
from tinymce.models import HTMLField
from users.models import User

class Order(models.Model):
    title = models.CharField(max_length = 255, verbose_name = 'Заказы')
    descriptiom = models.TextField(verbose_name = 'Описание')
    price = models.IntegerField(default = 0, verbose_name = 'Цена')
    performer = models.ForeignKey(User, verbose_name = 'Исполнитель', null = True, blank = True, on_delete = models.SET_NULL, related_name = 'order_performer')
    customer = models.ForeignKey(User, verbose_name = 'Заказчик', null = True, blank = True, on_delete = models.SET_NULL, related_name = 'order_customer')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы' 

    def __str__(self) -> str:
        return self.title


# Create your models here.
