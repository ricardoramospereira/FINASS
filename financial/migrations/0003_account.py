# Generated by Django 4.2.4 on 2023-08-15 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("financial", "0002_alter_category_essential_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "bank",
                    models.CharField(
                        choices=[
                            ("NU", "Nubank"),
                            ("CE", "Caixa econômica"),
                            ("SP", "Stone Pagamentos"),
                            ("BS", "Banco Cooperativo Sicredi S.A."),
                            ("AC", "Advanced Cc Ltda"),
                        ],
                        max_length=2,
                        verbose_name="Banco",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("PF", "Pessoa física"), ("PJ", "Pessoa Jurídica")],
                        max_length=2,
                        verbose_name="Tipo",
                    ),
                ),
                ("value", models.FloatField(verbose_name="Valor")),
            ],
        ),
    ]
