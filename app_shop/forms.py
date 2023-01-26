from django import forms
from django.forms import ModelForm
from app_shop.models import Productos


class LoadForm(ModelForm):
    class Meta:
        model = Productos
        fields = [
            "articulo",
            "producto",
            "stock_disponible",
            "precio_menor",
            "precio_mayor",
            "imagen",
            "categoria",
        ]

    def __init__(self, *args, **kwargs):
        super(LoadForm, self).__init__(*args, **kwargs)
