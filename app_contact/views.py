from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from app_contact.models import Consulta
from app_contact.forms import ConsultaForm

# dos importaciones son necesarias para trabajar con formularios
from django.views.generic import View
from django.views.generic import FormView


class Contacto(FormView):
    template_name = "app_contact/contact.html"
    form_class = ConsultaForm
    success_url = "successfull_contact"

    def form_valid(self, form):
        form.save()
        form.send_email()
        return super().form_valid(form)


class SuccessfullContact(View):
    template_name = "app_contact/successfull_contact.html"

    def get(self, request):
        params = {"Mensaje": "Hola"}
        return render(request, self.template_name, params)


# Create your views here.
def contact(request):
    return render(request, "app_contact/contact.html")
