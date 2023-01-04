from django.contrib import admin
from app_shop.models import Categorias
from app_shop.models import Productos


class ProductoInline(admin.TabularInline):
    model = Productos
    extra = 0


class CategoriaAdmin(admin.ModelAdmin):
    inlines = [ProductoInline]


@admin.register(Productos)
class ProductoAdmin(admin.ModelAdmin):
    # fields = ["categoria", "fecha_publicacion", "producto", "imagen"]

    fieldsets = [
        ("Relación", {"fields": ["categoria"]}),
        (
            "Datos generales",
            {
                "fields": [
                    "articulo",
                    "producto",
                    "stock_disponible",
                    "precio_menor",
                    "precio_mayor",
                    "imagen",
                ]
            },
        ),
    ]
    list_display = [
        "producto",
        # "fecha_publicacion",
    ]
    # ordering = ["-fecha_publicacion"]
    list_filter = (
        "producto",
        # "fecha_publicacion",
    )
    search_fields = (
        "producto",
        "estado",
    )
    list_display_links = (
        "producto",
        # "fecha_publicacion",
    )


admin.site.register(Categorias, CategoriaAdmin)
