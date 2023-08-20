from django.db import models

# Create your models here.
class Testimonial(models.Model):
    text = models.TextField()
    name = models.CharField(max_length=50)