# Generated by Django 4.2.17 on 2025-02-03 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0003_alter_catalogueitem_points_cost_redemptionitem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="redemptionitem",
            name="redemption",
            field=models.ForeignKey(
                help_text="The redemption transaction this item is part of.",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="catalogue.redemption",
            ),
        ),
    ]
