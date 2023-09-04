from django.db import models
from datetime import datetime


class Category(models.Model):
    category = models.CharField("categoria", max_length=50)
    essential = models.BooleanField("essêncial", default=False)
    planning_value = models.FloatField("Valor de planejamento", default=0)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self) -> str:
        return self.category
    
    def total_spent(self):
        from extract.models import Values
        values = Values.objects.filter(category_id=self.id).filter(date__month=datetime.now().month).aggregate(models.Sum('value'))
        return values['value__sum'] if values['value__sum'] else 0
    
    def calculate_percentage_spend_by_category(self):
        try:
            return int((self.total_spent() * 100) / self.planning_value)
        except ZeroDivisionError:
            return 0

        
class Account(models.Model):
    class Meta:
        verbose_name = "Conta"
        verbose_name_plural = "Contas"

    BANK_CHOICES = (
        ('Nu', 'Nubank'),
        ('BB', 'Banco do Brasil'),
        ('CE', 'Caixa Econômica Federal'),
        ('IT', 'Itaú Unibanco'),
        ('SA', 'Santander'),
        ('BR', 'Bradesco'),
        ('HS', 'HSBC'),
        ('CT', 'Citibank'),
        ('BN', 'BNDES'),
        ('BP', 'Banco Pan'),
        ('SC', 'Sicoob'),
        ('IN', 'Banco Inter'),
        ('CB', 'C6 Bank'),
        ('BancoOriginal', 'Banco Original'),
        ('SF', 'Banco Safra'),
        ('NE', 'Next'),
        ('NE', 'Neon'),
        ('BD', 'BTG Pactual'),
        ('BA', 'Banco Daycoval'),
        ('XP', 'XP Investimentos'),
        # Adicione mais bancos aqui...
    )


    ACCOUNT_TYPE = (
        ('PF', 'Pessoa física'),
        ('PJ', 'Pessoa Jurídica')
    )

    bank = models.CharField('Banco', max_length=20, choices=BANK_CHOICES)
    type = models.CharField('Tipo', max_length=2, choices=ACCOUNT_TYPE)
    value = models.FloatField('Valor', default=0)


    def __str__(self) -> str:
        return self.bank
    
    def get_full_bank_name(self):
        for choice in self.BANK_CHOICES:
            if choice[0] == self.bank:
                return choice[1]
        return self.bank  # Retorna a sigla se não encontrada na lista de escolhas