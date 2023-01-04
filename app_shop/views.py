from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from app_shop.models import Productos

# Create your views here.
def index(request):
    return render(request, "app_shop/index.html")


def contact(request):
    return render(request, "app_shop/contact.html")


def shop(request):
    prods = Productos.objects.all()
    info_prods = {"products": prods}
    return render(request, "app_shop/shop.html", info_prods)
