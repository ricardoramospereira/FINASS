# Generated by Django 4.2.4 on 2023-08-17 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("financial", "0006_alter_account_bank"),
    ]

    operations = [
        migrations.CreateModel(
            name="Values",
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
                ("value", models.FloatField(verbose_name="Valor")),
                ("description", models.TextField(verbose_name="Descrição")),
                ("date", models.DateField(verbose_name="Data")),
                (
                    "type",
                    models.CharField(
                        choices=[("E", "Entrada"), ("S", "Saída")],
                        max_length=1,
                        verbose_name="tipo",
                    ),
                ),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="financial.account",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="financial.category",
                    ),
                ),
            ],
        ),
    ]
