# Generated by Django 5.1 on 2025-02-04 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                    "name",
                    models.CharField(
                        db_index=True,
                        help_text="Category name",
                        max_length=32,
                        unique=True,
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        db_index=True, help_text="Category description", max_length=256
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, help_text="Date created"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, help_text="Last update"),
                ),
            ],
            options={
                "db_table": "categories",
            },
        ),
    ]
