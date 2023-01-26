from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from app_shop.models import Productos
from app_shop.forms import LoadForm
from django.shortcuts import redirect
from django.http import Http404
from django.views.generic import View

# Create your views here.
def index(request):
    return render(request, "app_shop/index.html")


def shop(request):
    prods = Productos.objects.all()
    info_prods = {"products": prods}
    return render(request, "app_shop/shop.html", info_prods)


def load_img(request):
    params = {}

    if request.method == "POST":
        form = LoadForm(request.POST, request.FILES)
        params["form"] = form
        if form.is_valid():
            articulo = form.cleaned_data["articulo"]
            producto = form.cleaned_data["producto"]
            stock_disponible = form.cleaned_data["stock_disponible"]
            precio_menor = form.cleaned_data["precio_menor"]
            precio_mayor = form.cleaned_data["precio_mayor"]
            imagen = form.cleaned_data["imagen"]
            categoria = form.cleaned_data["categoria"]

            new_prod = Productos(
                articulo=articulo,
                producto=producto,
                stock_disponible=stock_disponible,
                precio_menor=precio_menor,
                precio_mayor=precio_mayor,
                imagen=imagen,
                categoria=categoria,
            )
            new_prod.save()
            return redirect("shop/")
    else:
        print("Esta en el GET")
        form = LoadForm()
        params["form"] = form
        return render(request, "app_shop/load-prod.html", params)


class SeeImgs(View):
    template = "app_shop/see-img.html"

    def get(self, request):
        params = {}
        try:
            prods = Productos.objects.all()
        except Productos.DoesNotExist:
            raise Http404
        params["products"] = prods

        return render(request, self.template, params)


def see_prod(request, prod_id):
    params = {}
    try:
        prod = Productos.objects.get(id=prod_id)
    except Productos.DoesNotExist:
        raise Http404
    params["product"] = prod

    return render(request, "app_shop/see-prod.html", params)