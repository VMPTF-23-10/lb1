from django.contrib import admin

from .models import CurrencyRate


@admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    list_display = ('name', 'buy_rate', 'sell_rate', 'date')
    list_filter = ('date',)
    search_fields = ('name',)
    ordering = ('-date', 'name')
    fields = ('name', 'buy_rate', 'sell_rate', 'date')


admin.site.site_header = 'Адмін-панель Курсу валют'
admin.site.site_title = 'Курси валют'
admin.site.index_title = 'Керування курсами валют'
