# Generated by Django 3.2 on 2022-07-15 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_order_additional_shipping_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='additional_shipping_info',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
