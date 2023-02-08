"""ekan_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# importaciones desde el views
from app_shop.views import Shop
from .views import Order
from app_shop.views import load_img
from .views import SeeImgs
from .views import see_prod

urlpatterns = [
    path("", Shop.as_view(), name="shop"),
    path("order/", Order.as_view(), name="order"),
    path("loadprod/", load_img, name="loadprod"),
    path("seeimg/", SeeImgs.as_view(), name="see"),
    path("<int:prod_id>/see/", see_prod, name="seeprod"),
]
