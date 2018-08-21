from django.conf.urls import url
from django.contrib import admin

from .views import CardNumberValidationView, CardPasswordValidationView

app_name = 'cards'

urlpatterns = [
    url(r'^num/$', CardNumberValidationView.as_view(), name='num_validator'),
    url(r'^pass/$', CardPasswordValidationView.as_view(), name='pass_validator'),
]
