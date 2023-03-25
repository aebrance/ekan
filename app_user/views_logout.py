from django.shortcuts import render

# necesarias para controlar el inicio de sesion
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.shortcuts import redirect

# Create your views here.


def logout_management(request):
    params = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "app_user/logout.html", params)
    else:
        logout(request)
        return render(request, "app_user/logout.html", params)
