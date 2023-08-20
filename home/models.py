from django.db import models

# Create your models here.

class Home(models.Model):
    intro_text = models.TextField()
    video = models.CharField(max_length=50)
