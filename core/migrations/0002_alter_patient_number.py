# Generated by Django 3.2.4 on 2021-10-05 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="number",
            field=models.CharField(max_length=15),
        ),
    ]
