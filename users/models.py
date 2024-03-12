from django.db import models
from tinymce.models import HTMLField
from skills.models import Skill
from authorization.models import User

# class User(models.Model):
#     full_name = models.CharField(max_length = 255, verbose_name = 'Имя')
#     skills = models.ForeignKey(Skill, verbose_name = 'Навыки', null = True, blank = True, on_delete = models.SET_NULL,)

#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'

    
#     def __str__(self) -> str:
#         return self.full_name





