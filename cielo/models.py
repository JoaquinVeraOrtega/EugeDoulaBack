from django.db import models

# Create your models here.
class Cielo(models.Model):
    name = models.CharField( max_length=50)
    cover_img = models.CharField( max_length=150)
    subtitle = models.TextField()
    video = models.CharField( max_length=50)
    video_text = models.TextField()
    text1 = models.TextField()
    text2 = models.TextField()
    img1 = models.CharField( max_length=150)
    img1_text = models.TextField()
    