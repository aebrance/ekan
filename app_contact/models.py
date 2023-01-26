from django.db import models
from datetime import datetime
from django.utils.html import format_html

# Create your models here.
class Consulta(models.Model):
    RESPONDIDA = "Respondida"
    NORESPONDIDA = "No respondida"
    ENPROCESO = "En proceso"
    ESTADOS = (
        (RESPONDIDA, "Respondida"),
        (NORESPONDIDA, "No respondida"),
        (ENPROCESO, "En proceso"),
    )

    name = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)
    mail = models.EmailField(max_length=100, blank=False, null=False)
    estado_respuesta = models.CharField(
        max_length=15, choices=ESTADOS, default=NORESPONDIDA
    )
    telefono = models.CharField(max_length=100, blank=False, null=False)
    fecha = models.DateField(default=datetime.now, blank=True, editable=True)

    def __str__(self):
        return self.name

    def estado_de_resp(self):
        if self.estado_respuesta == "Respondida":
            return format_html(
                f"<span style='background-color: lightgreen; color: green; padding: 2px;'>{self.estado_respuesta}</span>"
            )
        elif self.estado_respuesta == "En proceso":
            return format_html(
                f"<span style='background-color: lightblue; color: blue; padding: 2px;'>{self.estado_respuesta}</span>"
            )
        else:
            return format_html(
                f"<span style='background-color: lightcoral; color: red; padding: 2px;'>{self.estado_respuesta}</span>"
            )


class Respuesta(models.Model):
    consulta = models.ForeignKey(
        Consulta(), blank=True, null=True, on_delete=models.CASCADE
    )
    respuesta = models.TextField(blank=False, null=False)
    fecha = models.DateField(default=datetime.now, blank=True, editable=True)

    def create_answer(self):
        consulta_cambio_estado = Consulta.objects.get(id=self.consulta.id)
        consulta_cambio_estado.estado_respuesta = "Respondida"
        consulta_cambio_estado.save()
        # AGREGAR LA LÓGICA PARA ENVIAR UN MAIL CON UN HTML

    def save(self, *args, **kwargs):
        self.create_answer()
        force_update = False
        if self.id:
            force_update = True
        super(Respuesta, self).save(force_update=force_update)
