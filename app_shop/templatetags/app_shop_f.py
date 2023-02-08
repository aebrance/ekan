from django import template
from pprint import pprint

register = template.Library()

# las funciones son los filtros
@register.filter(name="in_order")
def in_order(product, order):
    keys = order.keys()
    for id in keys:
        if int(id) == product.id:
            return order[id]
        else:
            return ""


@register.filter(name="make_invoice")
def make_invoice(product, order):
    pass


"""
Para cargar este filtros a un html se debe escribir al incio de este {% load app_contact_f %} 
dado que este el nombre del archivo """
