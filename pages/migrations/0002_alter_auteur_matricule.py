# Generated by Django 5.0.3 on 2024-05-15 06:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="auteur",
            name="matricule",
            field=models.IntegerField(default=0),
        ),
    ]