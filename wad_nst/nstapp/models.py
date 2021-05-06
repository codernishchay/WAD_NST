from django.db import models
from PIL import Image

class Image(models.Model):
    # user = models.ForeignKey(User)
    # description = models.CharField(max_length=200)
    image1 = models.ImageField(upload_to = 'style')
    image2 = models.ImageField(upload_to = 'base')
    image3 = models.ImageField(upload_to = 'generated')

