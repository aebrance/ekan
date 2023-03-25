from django import template

register = template.Library()

# las funciones son los filtros


@register.filter(name="in_order")
def in_order(product, order):
    keys = list(order.keys())
    for id in keys:
        if int(id) == product.id:
            return order[id]
        id = ""


@register.filter(name="make_invoice")
def make_invoice(product, order):
    pass


"""
Para cargar este filtros a un html se debe escribir al incio de este {% load app_contact_f %} 
dado que este el nombre del archivo """
