# Generated by Django 4.2.9 on 2024-01-27 11:33

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Host",
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
                (
                    "url",
                    models.CharField(max_length=255, verbose_name="URL или IP адрес"),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("extremist", "Террористический ресурс"),
                            ("fraud", "Мошенничество и фишинг"),
                            ("porn", "Порно"),
                            ("escort", "Эскорт"),
                        ],
                        db_index=True,
                        max_length=20,
                        verbose_name="Категория",
                    ),
                ),
                (
                    "risk_level",
                    models.CharField(
                        choices=[
                            ("whitelist", "Доверенный"),
                            ("blacklist", "Заблокированный"),
                            ("suspicious", "Подозрительный"),
                        ],
                        db_index=True,
                        max_length=20,
                        verbose_name="Уровень риска",
                    ),
                ),
            ],
            options={
                "verbose_name": "Хост",
                "verbose_name_plural": "Хосты",
                "db_table": "hosts",
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="Keyword",
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
                ("keyword", models.TextField(verbose_name="URL или IP адрес")),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("extremist", "Террористический ресурс"),
                            ("fraud", "Мошенничество и фишинг"),
                            ("porn", "Порно"),
                            ("escort", "Эскорт"),
                            ("curse", "Матерное слово"),
                        ],
                        db_index=True,
                        max_length=20,
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ключевое слово",
                "verbose_name_plural": "Ключевые слова",
                "db_table": "keywords",
                "ordering": ["-id"],
            },
        ),
    ]
