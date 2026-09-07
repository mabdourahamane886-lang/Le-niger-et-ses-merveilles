from django.shortcuts import render

from .models import Merveille


def accueil(request):
    merveilles = Merveille.objects.filter(publie=True).select_related("region")
    return render(request, "explorer/accueil.html", {"merveilles": merveilles})
