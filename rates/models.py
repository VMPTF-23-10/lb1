from django.db import models
from django.utils import timezone


class CurrencyRate(models.Model):
    name = models.CharField('Назва валюти', max_length=50)
    buy_rate = models.DecimalField('Курс купівлі', max_digits=10, decimal_places=2)
    sell_rate = models.DecimalField('Курс продажу', max_digits=10, decimal_places=2)
    date = models.DateField('Дата', default=timezone.localdate)

    class Meta:
        verbose_name = 'Курс валюти'
        verbose_name_plural = 'Курси валют'

    def __str__(self):
        return self.name
