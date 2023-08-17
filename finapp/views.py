from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def payments(request):
    return render(request, 'payments.html')


def analytics(request):
    return render(request, 'analytics.html')


def goals(request):
    return render(request, 'goals.html')


def more(request):
    return render(request, 'more.html')


def welcome(request):
    return render(request, 'welcome.html')


def transactions(request):
    return render(request, 'transactions.html')


def transaction_detail(request):
    return render(request, 'transaction_detail.html')
