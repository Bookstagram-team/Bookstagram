from django.db import models
# Create your models here.

class Event(models.Model):
    nama_event = models.CharField(max_length=255)
    tanggal_pelaksanaan = models.CharField(max_length=255)
    foto = models.CharField(max_length=255)
    harga = models.IntegerField()