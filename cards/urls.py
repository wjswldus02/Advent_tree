from django.urls import path

from . import views

app_name = "cards"

urlpatterns = [
    path("", views.all_card, name="all_card"),
    # path("create/", views.create_card, name="create_card"),
]
