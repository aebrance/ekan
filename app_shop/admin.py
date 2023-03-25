from django.contrib import admin
from app_shop.models import Categorias
from app_shop.models import Productos
from django.http import HttpResponse
from django.core import serializers

# se pasa a actions como string sólo cuando es un método de clase
# def change_article(modeladmin, request, queryset):
#     queryset.update(articulo="0000")


# change_article.short_description = "Cambiar artículo a default"


class ProductoInline(admin.TabularInline):
    model = Productos
    extra = 0


class CategoriaAdmin(admin.ModelAdmin):
    inlines = [ProductoInline]


@admin.register(Productos)
class ProductoAdmin(admin.ModelAdmin):
    # fields = ["categoria", "producto", "imagen"]

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
    ]
    # ordering = ["-fecha_publicacion"]
    list_filter = ("producto",)
    search_fields = (
        "producto",
        "estado",
    )
    list_display_links = ("producto",)
    # actions = [change_article]
    actions = ["change_article", "info_to_json"]

    def change_article(self, request, queryset):
        log = queryset.update(articulo="0000")
        if log == 1:
            msg = "Se ha modificado el artículo del producto seleccionado"
        else:
            msg = "Se han modificado los artículos de los productos seleccionados"

        self.message_user(request, msg + " exitosamente.")

    change_article.short_description = "Cambiar artículo a default"

    def info_to_json(self, request, queryset):
        response = HttpResponse(content_type="application/json")
        serializers.serialize("json", queryset, stream=response)
        return response

    info_to_json.short_description = "Información en formato JSON"


admin.site.register(Categorias, CategoriaAdmin)
