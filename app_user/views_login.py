from django.shortcuts import render
# si certifica las credenciales dadas, devuelve un objeto de la clase User
from django.contrib.auth import authenticate
# sirve para certificar credenciales
from django.contrib.auth import login
from django.shortcuts import redirect
# Create your views here.


def login_management(request):
    params = {}

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "app_user/login.html", params)

    return render(request, "app_user/login.html", params)
