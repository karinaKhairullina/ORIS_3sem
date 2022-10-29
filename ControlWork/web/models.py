from django.db import models


class ToDoList(models.Model):
    dbid = models.CharField(max_length=10, verbose_name='ID пользователя')
    to_do = models.CharField(max_length=30, verbose_name='Что сделать?')
    done = models.CharField(max_length=30, verbose_name='Что сделано?')
    created_at = models.CharField(max_length=30)
    until_date = models.DateField("Дата создания")

