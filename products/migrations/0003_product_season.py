# Generated by Django 3.2 on 2022-07-06 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='season',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
