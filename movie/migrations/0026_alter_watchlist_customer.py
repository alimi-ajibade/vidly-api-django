# Generated by Django 4.1.1 on 2022-10-05 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0025_watchlist_customer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="watchlist",
            name="customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="customer",
                to="movie.customer",
            ),
        ),
    ]
