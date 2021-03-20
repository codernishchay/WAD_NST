from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import redirect, render


def home(request):
    return render(request, "home.html")


def signupuser(request):
    if request.method == "GET":
        return render(request, "signupuser.html", {"forms": UserCreationForm()})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"]
                )
                user.save()
                # When user signed in redirect to new url.
                login(request, user)
                return redirect("about")

            except IntegrityError:
                return render(
                    request,
                    "signupuser.html",
                    {"forms": UserCreationForm(), "error": "Username is already taken try other!"},
                )

        else:
            # Tell the use user password didn't match.
            return render(
                request,
                "signupuser.html",
                {"forms": UserCreationForm(), "error": "Password did not match"},
            )


def about(request):
    return render(request, "about.html")


def logoutuser(request):
    logout(request)
    return redirect("home")


def loginuser(request):
    if request.method == "GET":
        return render(request, "loginuser.html", {"forms": AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST["username"], password=request.POST["password"]
        )
        if user is None:
            return render(
                request,
                "loginuser.html",
                {"forms": AuthenticationForm(), "error": "Username and password did not match"},
            )
        else:
            login(request, user)
            return redirect("home")
