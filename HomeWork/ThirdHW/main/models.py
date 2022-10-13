from django.db import models

# Create your models here.

class Salespeople(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    city = models.CharField(max_length=100, verbose_name='Город проживания')

#чтобы в админке высвечивались строки по красоте
    def __str__(self):
        return f' name: {self.name}, city:{self.city}'

class Customers(models.Model):
    FIO = models.CharField(max_length=100, help_text='Введите свое полное ФИО')
    number = models.IntegerField(verbose_name='Идентификатор')

    def __str__(self):
        return f'FIO: {self.FIO}, number:{self.number}'



