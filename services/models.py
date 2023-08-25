from django.db import models
from django.contrib.postgres.fields import ArrayField



# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    quote = models.TextField()
    author = models.TextField()
    cover_img = models.CharField(max_length=100)
    duration = models.CharField(max_length=100, null=True)
    modality = models.CharField(max_length=100, null=True)
    img1 = models.CharField(max_length=100, null=True)
    img2 = models.CharField(max_length=100, null=True)
    img3 = models.CharField(max_length=100, null=True)
    video = models.CharField(max_length=100, null=True)
    img1_text = models.TextField(null=True)
    img2_text = models.TextField(null=True)
    img3_text = models.TextField(null=True)
    video_text = models.TextField(null=True)

    class Meta:
        abstract = True
        
class Tejedora(Service):
    subtitle1 = models.TextField()
    subtitle2 = models.TextField()
    subtitle2_text = models.TextField()
    list1_title = models.TextField()
    list1 = ArrayField(models.CharField(max_length=550),null=True)
    list1bis = models.TextField(null=True)
    list2_title = models.TextField()
    list2 = ArrayField(models.CharField(max_length=550),null=True)
    list2bis = models.TextField(null=True)
    text = models.TextField()
    img3_text_author = models.TextField()

class RitosDePaso(Service):
    text = models.TextField()
    
class GestarParirAlumbrar(Service):
    list1_title = models.TextField()
    list1 = ArrayField(models.CharField(max_length=550),null=True)
    list1bis = models.TextField(null=True)
    subtitle1 = models.TextField()
    subtitle2 = models.TextField()
    list2_title = models.TextField()
    list2 = ArrayField(models.CharField(max_length=550),null=True)
    list2bis = models.TextField(null=True)
    list3_title = models.TextField()
    list3 = ArrayField(models.CharField(max_length=550),null=True)
    list3bis = models.TextField(null=True)
    list4_title = models.TextField()
    list4 = ArrayField(models.CharField(max_length=550),null=True)
    list4bis = models.TextField(null=True)
    list5_title = models.TextField()
    list5 = ArrayField(models.CharField(max_length=550),null=True)
    list5bis = models.TextField(null=True)
    
class Flores(Service):
    subtitle = models.TextField()
    text = models.TextField()
    acknowledgments = models.TextField()
    
class HierbasBañosYVapores(Service):
    subtitle = models.TextField()
    text1 = models.TextField()
    text2 = models.TextField()
    acknowledgments = models.TextField()
    
class DueloGestacional(Service):
    subtitle = models.TextField()
    text = models.TextField()
    
class Masaje(Service):
    subtitle1 = models.TextField()
    subtitle1_text = models.TextField()
    acknowledgments = models.TextField()
    
class RitualCerrada(Service):
    text1 = models.TextField()
    text2 = models.TextField()
    
class Cartografia(Service):
    text1 = models.TextField()
    list_title = models.TextField()
    list = ArrayField(models.CharField(max_length=550),null=True)
    listbis = models.TextField(null=True)
    
class Alquimia(Service):
    subtitle = models.TextField()
    text1 = models.TextField()
    text2 = models.TextField()
    list1_title = models.TextField()
    list1 = ArrayField(models.CharField(max_length=550),null=True)
    list1bis = models.TextField(null=True)
    list2_title = models.TextField()
    list2 = ArrayField(models.CharField(max_length=550),null=True)
    list2bis = models.TextField(null=True)