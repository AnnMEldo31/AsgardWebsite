# Generated by Django 4.1.1 on 2022-09-22 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("asgard", "0003_auto_20220921_1905"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
