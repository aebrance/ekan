from django.shortcuts import render
from django.shortcuts import redirect
from app_user.forms import CreateUserForm


def register(request):
    params = {}
    form = CreateUserForm()
    params["form"] = form

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            return redirect("register")

    return render(request, "app_user/register.html", params)
