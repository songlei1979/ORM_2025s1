# Generated by Django 5.1.7 on 2025-03-17 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lesson", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="header_image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AddField(
            model_name="post",
            name="snippet",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        ),
    ]
