from django.db import models
from django.utils import timezone


class Currency(models.Model):
    code = models.CharField('Код валюти', max_length=10, unique=True)
    name = models.CharField('Назва валюти', max_length=100)

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюти'
        ordering = ('code',)

    def __str__(self):
        return f'{self.code} - {self.name}'


class CurrencyRate(models.Model):
    currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        verbose_name='Валюта',
        null=True,
    )
    buy_rate = models.DecimalField('Курс купівлі', max_digits=10, decimal_places=2)
    sell_rate = models.DecimalField('Курс продажу', max_digits=10, decimal_places=2)
    date = models.DateField('Дата', default=timezone.localdate)

    class Meta:
        verbose_name = 'Курс валюти'
        verbose_name_plural = 'Курси валют'

    def __str__(self):
        if self.currency:
            return f'{self.currency.code} ({self.date})'
        return f'Курс без валюти ({self.date})'
