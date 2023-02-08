from django.shortcuts import render
from django.views.generic import View


class Greet(View):
    template = "app_greet/index.html"

    def get(self, request):
        params = {}
        return render(request, self.template, params)
