# Generated by Django 3.2.4 on 2021-10-03 03:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_auto_20211001_2243"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="appointment",
            options={
                "ordering": ["-id"],
                "verbose_name": "appointment",
                "verbose_name_plural": "appointments",
            },
        ),
        migrations.AlterModelOptions(
            name="patient",
            options={
                "ordering": ["-id"],
                "verbose_name": "patient",
                "verbose_name_plural": "patients",
            },
        ),
        migrations.AddField(
            model_name="appointment",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="appointment",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]