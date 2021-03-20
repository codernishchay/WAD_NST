from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="homepage"),
    path("about/", views.about, name="about"),
    path("login/", views.loginuser, name="logininuser"),
    path("logout/", views.logoutuser, name="logoutuser"),
    path("signup/", views.signupuser, name="signupuser"),
]
