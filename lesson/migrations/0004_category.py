# Generated by Django 5.1.7 on 2025-03-17 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lesson", "0003_alter_post_snippet"),
    ]

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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=50)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
