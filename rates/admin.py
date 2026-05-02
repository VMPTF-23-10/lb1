from django.contrib import admin

from .models import Currency, CurrencyRate


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')
    ordering = ('code',)


@admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    list_display = ('currency', 'buy_rate', 'sell_rate', 'date')
    list_filter = ('date', 'currency')
    search_fields = ('currency__code', 'currency__name')
    ordering = ('-date', 'currency__code')
    fields = ('currency', 'buy_rate', 'sell_rate', 'date')


admin.site.site_header = 'Адмін-панель курсу валют'
admin.site.site_title = 'Курс валют'
admin.site.index_title = 'Керування курсами валют'
