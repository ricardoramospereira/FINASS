from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField("categoria", max_length=50)
    essential = models.BooleanField("essêncial", default=False)
    planning_value = models.FloatField("Valor de planejamento", default=0)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self) -> str:
        return self.category
        
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