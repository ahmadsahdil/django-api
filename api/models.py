from django.db import models

class Kelompok(models.Model):
    nama =models.CharField(max_length=10)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama
