# Generated by Django 4.2.9 on 2024-01-27 20:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0004_alter_host_category_alter_keyword_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="keyword",
            name="search_place",
            field=models.CharField(
                choices=[("URL", "URL"), ("CONTENT", "Контент"), ("ALL", "Все")],
                db_index=True,
                default="ALL",
                max_length=20,
                verbose_name="Место поиска",
            ),
        ),
    ]
