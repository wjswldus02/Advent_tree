from django.core.serializers import serialize
from django.http import HttpResponse
# from django.shortcuts import render, redirect, reverse
from django.views.generic import FormView
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny

from . import models, serializers


# def all_card(request):
#     qs = models.Card.objects.all()
#     data = serialize("json", qs, fields=('writer', 'content', 'reg_date'))
#     # return render(request, "cards.html", {"cards": data})
#     # return HttpResponse(data, content_type="application/json")
#     form = forms.CreateCardForm(request.POST)
#     return render(request, "cards.html", {"fields": form, "cards": data})


# def create_card(request):
#     if request.method == "POST":
#         form = forms.CreateCardForm(request.POST)
#         form.save()
#         return redirect(reverse("cards:all_card"))


class CardViewSet(viewsets.ModelViewSet):
    queryset = models.Card.objects.all()
    serializer_class = serializers.CardSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter]
    search_fields = ["week"]
    ...
