from django.db import models
from financial.models import Account, Category

# Create your models here.
class Values(models.Model):
    class Meta:
        verbose_name = 'Valor'
        verbose_name_plural = 'Valores'

    CHOICE_TYPE = (
        ('E', 'Entrada'),
        ('S', 'Saída')
    )

    value = models.FloatField('Valor')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.TextField('Descrição')
    date = models.DateField('Data')
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    type = models.CharField('tipo', max_length=1, choices=CHOICE_TYPE)

    def __str__(self) -> str:
        return self.description