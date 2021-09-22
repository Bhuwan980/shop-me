from .models import *


def category_menu(request):
    links = Categories.objects.all()
    return dict(links=links)