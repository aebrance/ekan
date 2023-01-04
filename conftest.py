"""Permite generar los fixture fuera de los archivos test; no hay necesidad de importarlos"""
import pytest
from app_shop.models import Productos
from app_shop.models import Categorias
import datetime  # esto se importa debido a que la base de datos productos tiene un campo de fechas
from pprint import pprint
from faker import Faker

fake = Faker()  # permite generar datos falsos


@pytest.fixture()
def crear_producto(db):
    mi_prod = Productos(producto="Calza")
    mi_prod.save()
    return mi_prod


@pytest.fixture()
def crear_producto_factory(db):
    cat1 = Categorias(nombre="Categoria 1", slug="cat1")
    cat1.save()

    def crear_producto(fecha_publicacion=datetime.datetime.now(), categoria=cat1):
        mi_prod = Productos(fecha_publicacion=fecha_publicacion, categoria=categoria)
        mi_prod.save()
        return mi_prod

    return crear_producto


@pytest.fixture()
def producto(db, crear_producto_factory):
    return crear_producto_factory(datetime.datetime.now())
