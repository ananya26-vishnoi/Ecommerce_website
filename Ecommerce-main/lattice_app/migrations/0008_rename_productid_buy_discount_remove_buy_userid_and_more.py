# Generated by Django 4.0.4 on 2022-05-06 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lattice_app', '0007_buy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buy',
            old_name='productid',
            new_name='discount',
        ),
        migrations.RemoveField(
            model_name='buy',
            name='userid',
        ),
        migrations.AddField(
            model_name='buy',
            name='price',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buy',
            name='product_id',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buy',
            name='product_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buy',
            name='user_id',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buy',
            name='username',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
