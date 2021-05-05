import os
import sys

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.shortcuts import render, redirect
from .models import Category, Photo
# Create your views here.

PACKAGE_PARENT = ".."
SCRIPT_DIR = os.path.dirname(
    os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__)))
)
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from nstapp.ML.nst_run import run


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


def gallery(request):
    return render(request, "gallery.html")


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




def upload(request):
    context = {}
    if request.method == "POST":
        uploaded_file = request.FILES["image"]
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        context["url"] = fs.url(name)
        print(url)
        print(uploaded_file.size)
    return render(request, "upload.html")


def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )

        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'add.html', context)