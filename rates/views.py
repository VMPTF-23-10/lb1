from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.utils import timezone

from .models import Currency, CurrencyRate


def rate_list(request):
    today = timezone.localdate()

    if request.method == 'POST':
        currency_id = request.POST.get('currency')
        buy_rate = request.POST.get('buy_rate')
        sell_rate = request.POST.get('sell_rate')
        date = request.POST.get('date') or today

        if currency_id and buy_rate and sell_rate:
            CurrencyRate.objects.create(
                currency_id=currency_id,
                buy_rate=buy_rate,
                sell_rate=sell_rate,
                date=date,
            )
            return redirect('rate_list')

    currencies = Currency.objects.all()
    rates = CurrencyRate.objects.filter(
        date=today,
        currency__isnull=False,
    ).order_by('currency__code')
    context = {
        'currencies': currencies,
        'rates': rates,
        'today': today,
        'active_tab': 'today',
    }
    return render(request, 'rates/rate_list.html', context)


def archive(request):
    rates = CurrencyRate.objects.filter(
        currency__isnull=False,
    ).order_by('-date', 'currency__code')
    context = {
        'rates': rates,
        'active_tab': 'archive',
    }
    return render(request, 'rates/archive.html', context)


def today_rates_api(request):
    today = timezone.localdate()
    rates = CurrencyRate.objects.filter(
        date=today,
        currency__isnull=False,
    ).order_by('currency__code')

    data = {
        'date': today.isoformat(),
        'rates': [
            {
                'code': rate.currency.code,
                'name': rate.currency.name,
                'buy_rate': str(rate.buy_rate),
                'sell_rate': str(rate.sell_rate),
            }
            for rate in rates
        ],
    }

    return JsonResponse(data)
