# Generated by Django 4.1.1 on 2022-11-16 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0033_videolink"),
    ]

    operations = [
        migrations.AlterField(
            model_name="videolink",
            name="link",
            field=models.URLField(blank=True),
        ),
    ]
