# Generated by Django 4.1.6 on 2023-02-15 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api", "0006_orderitem_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="ordered",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="orderitem",
            name="quantity",
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name="orderitem",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="UserOrdering",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
