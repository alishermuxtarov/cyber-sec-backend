# Generated by Django 4.2.9 on 2024-01-27 12:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0002_keyword_allowed_for_host"),
    ]

    operations = [
        migrations.AlterField(
            model_name="host",
            name="category",
            field=models.CharField(
                choices=[
                    ("extremist", "Террористический ресурс"),
                    ("fraud", "Мошенничество и фишинг"),
                    ("porn", "Порно"),
                    ("escort", "Эскорт"),
                    ("other", "Другое"),
                ],
                db_index=True,
                max_length=20,
                verbose_name="Категория",
            ),
        ),
    ]
