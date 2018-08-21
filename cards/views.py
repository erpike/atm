from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.detail import SingleObjectMixin

from .models import Card


# Create your views here.
class CardNumberValidationView(SingleObjectMixin, View):
    model = Card

    def get_object(self):
        number = self.request.GET.get('card')
        try:
            card = Card.objects.get(number=number)
            return card
        except:
            return None

    def get(self, request, *args, **kwargs):
        card = self.get_object()
        if not card:
            messages.error(self.request, 'Incorrect card data')
            return HttpResponseRedirect('/')
        else:
            return render(request, 'cards/card-password.html', {})