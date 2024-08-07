from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.


def user_login(request):
    # future -> ?next=/articles/create/
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print(request.user.is_authenticated)
            login(request, user)
            return redirect("/dashboard")
    else:
        form = AuthenticationForm(request)
    context = {"form": form}
    return render(request, "users/login.html", context)


def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login")
    return render(request, "users/logout.html", {})
