from django.shortcuts import render


def index(request):
    """
    View function for the site homepage.
    """
    return render(request, 'index.html', context={})
