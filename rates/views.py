from django.shortcuts import redirect, render
from django.utils import timezone

from .models import CurrencyRate


def rate_list(request):
    today = timezone.localdate()

    if request.method == 'POST':
        name = request.POST.get('name')
        buy_rate = request.POST.get('buy_rate')
        sell_rate = request.POST.get('sell_rate')
        date = request.POST.get('date') or today

        if name and buy_rate and sell_rate:
            CurrencyRate.objects.create(
                name=name,
                buy_rate=buy_rate,
                sell_rate=sell_rate,
                date=date,
            )
            return redirect('rate_list')

    rates = CurrencyRate.objects.filter(date=today).order_by('name')
    context = {
        'rates': rates,
        'today': today,
        'active_tab': 'today',
    }
    return render(request, 'rates/rate_list.html', context)


def archive(request):
    rates = CurrencyRate.objects.all().order_by('-date', 'name')
    context = {
        'rates': rates,
        'active_tab': 'archive',
    }
    return render(request, 'rates/archive.html', context)
