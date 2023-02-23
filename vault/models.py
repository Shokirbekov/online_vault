from django.db import models
from django.contrib.auth.models import User

class Ombor(models.Model):
    nom = models.CharField(max_length=500)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    tel = models.PositiveIntegerField()
    ism = models.CharField(max_length=150)
    manzil = models.CharField(max_length=1000)
    def __str__(self):
        return f"{self.nom}"

class Mahsulot(models.Model):
    nom = models.CharField(max_length=150)
    brend = models.CharField(max_length=200)
    narx = models.PositiveIntegerField()
    kelgan_sana = models.DateField()
    miqdor = models.PositiveIntegerField()
    olchov = models.CharField(max_length=500)
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nom}({self.ombor})"

class Client(models.Model):
    ism = models.CharField(max_length=150)
    nom = models.CharField(max_length=150)
    manzil = models.CharField(max_length=500)
    tel = models.PositiveIntegerField()
    qarz = models.PositiveIntegerField()
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)