# Generated by Django 4.1.2 on 2023-07-12 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("map_pins", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mappin",
            name="category",
            field=models.IntegerField(
                choices=[
                    (1, "1"),
                    (2, "2"),
                    (3, "3"),
                    (4, "4"),
                    (5, "5"),
                    (6, "6"),
                    (7, "7"),
                ]
            ),
        ),
    ]
