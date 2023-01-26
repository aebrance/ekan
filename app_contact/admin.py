from django.contrib import admin
from app_contact.models import Respuesta
from app_contact.models import Consulta

# Register your models here.


class RespuestaInline(admin.TabularInline):
    model = Respuesta
    extra = 0


# @admin.register(Respuesta)
# class RespuestaAdmin(admin.ModelAdmin):
#     list_display = [
#         "consulta",
#         "fecha",
#     ]
#     ordering = ["fecha"]


@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    inlines = [RespuestaInline]
    list_display = [
        "name",
        "fecha",
        "estado_de_resp",
    ]
    ordering = ["estado_respuesta", "-fecha"]
    list_filter = ("estado_respuesta", "fecha")
    search_fields = (
        "estado_respuesta",
        "fecha",
    )
