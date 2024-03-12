# Generated by Django 5.0.2 on 2024-03-12 12:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='', max_length=50, unique=True, verbose_name='Номер телефона (логин)')),
                ('role', models.IntegerField(choices=[(1, 'Суперадмин'), (2, 'Курьер'), (3, 'Покупатель')], default=3, verbose_name='Роль')),
                ('first_name', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='ФИО')),
                ('email', models.EmailField(blank=True, default='', max_length=100, null=True, verbose_name='Email')),
                ('date_joined', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата присоединения')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(choices=[(True, 'Не заблокирован'), (False, 'Заблокирован')], default=True, verbose_name='Статус доступа')),
                ('blocked', models.BooleanField(default=False, verbose_name='Пользователь заблокирован')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]