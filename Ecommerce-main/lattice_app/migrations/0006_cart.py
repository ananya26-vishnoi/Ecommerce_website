# Generated by Django 4.0.4 on 2022-05-04 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lattice_app', '0005_admin_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=100)),
                ('userid', models.CharField(max_length=100)),
            ],
        ),
    ]
