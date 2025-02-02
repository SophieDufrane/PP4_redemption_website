# Generated by Django 4.2.17 on 2025-02-02 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("catalogue", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Redemption",
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
                    "redeemed_on",
                    models.DateTimeField(
                        auto_now_add=True, help_text="The date and time of redemption."
                    ),
                ),
                (
                    "total_points_spent",
                    models.PositiveIntegerField(
                        help_text="Total points used for this redemption."
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="User who made the redemption.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
