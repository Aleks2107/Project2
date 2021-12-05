from django.db import models
from django.forms import DateInput


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Наименование')
    auther = models.CharField(max_length=50, verbose_name='Автор')
    genre = models.CharField(max_length=50, verbose_name='Жанр')
    status = models.TextField(null=True, blank=True, verbose_name='Описание')
    data = models.CharField(max_length=50, verbose_name='Данные абонента')
    give_out = models.CharField(max_length=50, verbose_name='Дата выдачи')
    give_in = models.CharField(max_length=50, verbose_name='Дата возврата')
    #rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'База данных'
        verbose_name = 'Поле данных'
        ordering = ['-give_in']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Статус')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Статус'
        ordering = ['name']
