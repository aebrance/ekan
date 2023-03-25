import json
from django.http import HttpResponse
from app_shop.models import Productos


def add(request, *args, **kwargs):
    if request.method == "GET":
        id_product = request.GET.get("productID")
        value = request.GET.get("qtyProduct")
        remove_item = request.GET.get("removeItem")
        cart = request.session.get("cart")
        id_product_rec = id_product[4:]
        id_product_rec = int(id_product_rec)
        products = Productos.objects.get(id=id_product_rec)
        available_stock = products.stock_disponible

        if remove_item == "true":
            if int(value) > 0:
                qty = int(value) - 1
                print(f"Le resta uno a: {value}")
            elif int(value) == 0:
                qty = int(value)
        else:
            if int(value) >= available_stock:
                qty = int(value)
            else:
                qty = int(value) + 1

        cart[id_product] = qty
        request.session["cart"] = cart
        print(f"(desde views_stock) Esto es lo que hay en  {request.session['cart']}")
        results = []
        data = {}
        data["id_product"] = str(id_product)
        data["qty"] = str(qty)
        results.append(data)
        data_json = json.dumps(results)
        mimetype = "application/json"
        return HttpResponse(data_json, mimetype)
