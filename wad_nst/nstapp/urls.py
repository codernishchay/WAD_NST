from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("login/", views.loginuser, name="loginuser"),
    path("logout/", views.logoutuser, name="logoutuser"),
    path("signup/", views.signupuser, name="signupuser"),
    path("gallery/", views.gallery, name="gallery"),
    path("upload/", views.upload, name="upload"),
    path('add/', views.addPhoto, name='add'),
]

# if settings.DEBUG:
#     urlpatterns+=static.(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)