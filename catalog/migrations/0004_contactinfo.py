# Generated by Django 5.1.2 on 2024-10-14 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_contact"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactInfo",
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
                ("name", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("address", models.TextField()),
            ],
        ),
    ]
