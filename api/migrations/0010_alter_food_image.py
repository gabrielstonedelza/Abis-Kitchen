# Generated by Django 4.1.6 on 2023-02-18 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0009_alter_orderitem_quantity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="food",
            name="image",
            field=models.ImageField(blank=True, upload_to="images"),
        ),
    ]
