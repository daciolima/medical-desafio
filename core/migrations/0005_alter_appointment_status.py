# Generated by Django 3.2.4 on 2021-10-03 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_alter_appointment_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="status",
            field=models.CharField(
                choices=[
                    ("not_confirme", "A Confirmar"),
                    ("Confirmado", "Confirmado"),
                    ("Finalizado", "Finalizado"),
                ],
                max_length=20,
            ),
        ),
    ]
