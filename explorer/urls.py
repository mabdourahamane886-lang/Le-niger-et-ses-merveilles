from django.urls import path

from .views import accueil

app_name = "explorer"
urlpatterns = [path("", accueil, name="accueil")]
