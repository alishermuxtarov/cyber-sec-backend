# Generated by Django 4.2.9 on 2024-01-27 11:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="keyword",
            name="allowed_for_host",
            field=models.CharField(
                max_length=255, null=True, verbose_name="Разрешен для хоста"
            ),
        ),
    ]
