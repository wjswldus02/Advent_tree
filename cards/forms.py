from django import forms

from . import models


class CreateCardForm(forms.ModelForm):
    class Meta:
        model = models.Card
        fields = ("writer", "content")
    
    def save(self, *args, **kwargs):
        card = super().save()
        return card
