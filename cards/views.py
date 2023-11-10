from django.shortcuts import render





def all_card(request):
    return render(request, 'cards/card_form.html', {})




