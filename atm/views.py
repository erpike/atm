from django.shortcuts import render


def home(request):
    return render(request, 'cards/card-number.html', {})