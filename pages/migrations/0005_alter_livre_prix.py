# Generated by Django 5.0.3 on 2024-05-15 12:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0004_alter_livre_fichier_pdf_alter_livre_photo_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="livre",
            name="prix",
            field=models.IntegerField(default=0),
        ),
    ]