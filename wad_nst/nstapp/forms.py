from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Image

class ImageForm(ModelForm):
    class Meta :
        model = Image
        fields = ['image1','image2','image3']