from django import forms
from django.forms import ModelForm
from app_contact.models import Consulta
from captcha.fields import CaptchaField


class ConsultaForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Consulta
        fields = [
            "name",
            "descripcion",
            "mail",
            # "estado_respuesta",
            "telefono",
            # "fecha",
        ]

    def send_email(self):
        name = self.cleaned_data["name"]
        descripcion = self.cleaned_data["descripcion"]
        mail = self.cleaned_data["mail"]
        # estado_respuesta = self.cleaned_data["estado_respuesta"]
        telefono = self.cleaned_data["telefono"]
        # fecha = self.cleaned_data["fecha"]

        # ACÁ HAY QUE AGREGAR LA LÓGICA PARA ENVIAR EL MAIL
