import pytest
from app_shop.models import Productos
from app_shop.models import Categorias
import datetime  # esto se importa debido a que la base de datos productos tiene un campo de fechas
from pprint import pprint


# lo lleve a conftest.py
# @pytest.fixture()
# def crear_producto(db):
#     mi_prod = Productos(producto="Calza", fecha_publicacion=datetime.datetime.now())
#     mi_prod.save()
#     return mi_prod


@pytest.mark.django_db
def test_cambiar_prod(crear_producto):
    print("Cambio de producto")
    assert crear_producto.producto == "Calza"


# @pytest.mark.django_db  # permite trabajar con las bases de datos
# def test_new_product():  # esta funcion no persiste los datos en la base de datos
#     mi_producto = Productos()
#     mi_producto_2 = Productos(
#         articulo="0001",
#         producto="Remera",
#         stock_disonible=100,
#         precio_menor=155.5,
#         precio_mayor=120.5,
#         fecha_publicacion=datetime.datetime.now(),
#     )
#     mi_producto.save()
#     mi_producto_2.save()
#     pprint(mi_producto)
#     pprint(mi_producto_2)
#     assert mi_producto_2.producto == mi_producto.producto


@pytest.mark.django_db
def test_cambiar_cat(producto):
    print(producto.fecha_publicacion)
    assert producto.categoria == "Categoria 2"
