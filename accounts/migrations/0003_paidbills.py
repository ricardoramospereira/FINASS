# Generated by Django 4.2.4 on 2023-09-05 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_bill_to_pay_bill_day_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="PaidBills",
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
                ("date_bill", models.DateField()),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="accounts.bill_to_pay",
                    ),
                ),
            ],
        ),
    ]
