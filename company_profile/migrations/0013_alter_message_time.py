# Generated by Django 4.1 on 2022-10-24 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("company_profile", "0012_alter_message_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="time",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
