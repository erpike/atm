from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from django.views.generic.base import View
from django.views.generic.detail import SingleObjectMixin

from .models import Card


# Create your views here.
class CardNumberValidationView(SingleObjectMixin, View):
    model = Card

    def get_object(self):
        number = self.request.POST.get('card')
        try:
            card = Card.objects.get(number=number)
            return card
        except:
            return None

    def post(self, request, *args, **kwargs):
        card = self.get_object()
        if not card:
            messages.error(self.request, 'Incorrect card data')
            return HttpResponseRedirect('/')
        else:
            request.session['card_number'] = card.number
            return HttpResponseRedirect(reverse('cards:pass_validator'))
            #return render(request, 'cards/card-password.html', {})


class CardPasswordValidationView(SingleObjectMixin, View):
    model = Card

    def get(self, request):
        return render(request, 'cards/card-password.html', {})

    def post(self, request):
        number = request.session.get('card_number')
        print(number)
        print(request.POST)
        print(request.POST.get('pass'))
        return render(request, 'cards/card-password.html', {})
