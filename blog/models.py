from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    intro = models.CharField(max_length=400)
    img = models.CharField(max_length=400)
    text = models.TextField()
    creation_date = models.DateField(auto_now_add=True)


