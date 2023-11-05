from django.shortcuts import render
from django.views.generic import View

from . import models

# Create your views here.
class CardView(View):
    model = models.Card
