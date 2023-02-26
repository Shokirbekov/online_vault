from django.db import models
from vault.models import *

class Statistika(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    miqdor = models.PositiveIntegerField()
    sana = models.DateTimeField(auto_now_add=True)
    umumiy_summa = models.PositiveBigIntegerField()
    tolandi = models.PositiveBigIntegerField()
    nasiya = models.PositiveBigIntegerField()
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f"{self.client}({self.ombor})"