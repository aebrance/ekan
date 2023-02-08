from django.shortcuts import render
from django.contrib.auth import logout
# Create your views here.


def logout_management(request):
    params = {}
    logout(request)
    return render(request, "app_user/logout.html", params)
