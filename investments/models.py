from django.db import models
from datetime import datetime

# Create your models here.
class Investment(models.Model):
    name = models.CharField("Nome", max_length=100)
    value = models.FloatField("Valor")
    status = models.BooleanField("Pago", default=False)
    date = models.DateField("Data", default=datetime.now)
    description = models.TextField("Descrição", max_length=255, blank=True)

    class Meta:
        verbose_name = "Investimento"
        verbose_name_plural = "Investimentos"

    def __str__(self) -> str:
        return self.name