# Generated by Django 5.0.6 on 2024-06-25 17:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="img_url",
            field=models.URLField(null=True),
        ),
    ]
