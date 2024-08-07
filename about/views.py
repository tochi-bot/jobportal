from django.shortcuts import render, redirect
from .models import About


def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_at').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )