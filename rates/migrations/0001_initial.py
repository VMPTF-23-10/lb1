# Generated for split commit part 1

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Назва валюти')),
                ('buy_rate', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Курс купівлі')),
                ('sell_rate', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Курс продажу')),
                ('date', models.DateField(default=django.utils.timezone.localdate, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Курс валюти',
                'verbose_name_plural': 'Курси валют',
            },
        ),
    ]
