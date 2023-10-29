from django.db import models

# Create your models here.
class Book(models.Model):
    Urutan = models.IntegerField()
    ISBN = models.CharField(max_length=255)
    Judul = models.CharField(max_length=255)
    Penulis = models.CharField(max_length=255)
    Publikasi = models.IntegerField()
    Publisher = models.CharField(max_length=255)
    ImageS = models.CharField(max_length=255)
    ImageM = models.CharField(max_length=255)
    ImageL = models.CharField(max_length=255)
    rating = models.IntegerField()

