from django.shortcuts import get_object_or_404, render

from .models import MediaGalerie, Merveille, Region


def accueil(request):
    context = {
        "regions": Region.objects.all(),
        "a_la_une": Merveille.objects.filter(
            publie=True, est_a_la_une=True
        ).select_related("region")[:6],
        "medias": MediaGalerie.objects.filter(publie=True).select_related("region")[:12],
    }
    return render(request, "explorer/accueil.html", context)


def region_detail(request, slug):
    region = get_object_or_404(Region, slug=slug)
    return render(
        request,
        "explorer/region_detail.html",
        {
            "region": region,
            "merveilles": region.merveilles.filter(publie=True),
            "medias": region.medias.filter(publie=True),
        },
    )


def merveille_detail(request, slug):
    merveille = get_object_or_404(Merveille, slug=slug, publie=True)
    return render(
        request,
        "explorer/merveille_detail.html",
        {"merveille": merveille},
    )
