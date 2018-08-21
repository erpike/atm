from django.conf.urls import url
from django.contrib import admin

from .views import CardNumberValidationView

app_name = 'cards'

urlpatterns = [
    url(r'^$', CardNumberValidationView.as_view(), name='num_validator'),
]
