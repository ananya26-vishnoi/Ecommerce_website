# Generated by Django 4.0.4 on 2022-05-03 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lattice_app', '0004_category_product_category_product_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='views',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
