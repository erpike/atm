from django.http import HttpResponseForbidden

from .models import Card


class CardNumberMixin(object):
    def dispatch(self, request, *args, **kwargs):
        number = request.session.get('number')
        if not number:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)