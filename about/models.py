from django.db import models

# Create your models here.
class About(models.Model):
    profile_pic = models.CharField( max_length=150)
    title = models.TextField()
    text = models.TextField()
    quote = models.TextField(null=True)
    email = models.EmailField( max_length=254, null=True)
    instagram = models.URLField( max_length=200, null=True)
    facebook = models.URLField( max_length=200, null=True)
    youtube = models.URLField( max_length=200, null=True)