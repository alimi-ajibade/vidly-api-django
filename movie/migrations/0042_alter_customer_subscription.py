# Generated by Django 4.1.3 on 2022-11-30 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0041_alter_customer_subscription"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="subscription",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="movie.subcriptiontype"
            ),
        ),
    ]