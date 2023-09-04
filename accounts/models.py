from django.db import models
from financial.models import Category

# Create your models here.
class Bill_to_pay(models.Model):
    class Meta:
        verbose_name = 'Dia do Pagamento'
        verbose_name_plural = 'Dias dos Pagamentos'

    title = models.CharField('Título', max_length=50)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.TextField('Descrição')
    value = models.FloatField('Valor')
    bill_day = models.IntegerField('Dia do pagamento')


    def __str__(self) -> str:
        return self.title

    