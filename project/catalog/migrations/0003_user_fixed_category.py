# Generated by Django 4.2.1 on 2023-05-08 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0002_alter_user_role"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="fixed_category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="catalog.category",
            ),
        ),
    ]
