from django.urls import path

from .views import accueil, merveille_detail, region_detail

app_name = "explorer"

urlpatterns = [
    path("", accueil, name="accueil"),
    path("regions/<slug:slug>/", region_detail, name="region_detail"),
    path("merveilles/<slug:slug>/", merveille_detail, name="merveille_detail"),
]
