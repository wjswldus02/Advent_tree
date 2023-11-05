from django.urls import path

from . import views

app_name = "cards"

urlpatterns = [
    path("", views.CardView.as_view(), name="all_review")
]
