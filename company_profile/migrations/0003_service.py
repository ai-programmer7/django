# Generated by Django 4.1 on 2022-10-10 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("company_profile", "0002_company_info_bottom_left"),
    ]

    operations = [
        migrations.CreateModel(
            name="Service",
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
                ("service_name", models.CharField(max_length=35)),
                ("title", models.CharField(max_length=35)),
                ("short_info", models.CharField(max_length=35)),
                ("description", models.CharField(max_length=250)),
            ],
        ),
    ]