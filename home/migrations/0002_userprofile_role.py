# Generated by Django 4.2.17 on 2025-01-31 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="role",
            field=models.CharField(
                choices=[("admin", "Admin"), ("employee", "Employee")],
                default="employee",
                max_length=10,
            ),
        ),
    ]
