# Generated by Django 4.1.1 on 2022-10-11 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0030_delete_customer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subcriptiontype",
            name="devices",
            field=models.CharField(default="Mobile", max_length=255),
        ),
    ]
