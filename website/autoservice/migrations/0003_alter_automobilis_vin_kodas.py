# Generated by Django 4.1.1 on 2022-09-30 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0002_uzsakymu_eilute'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automobilis',
            name='vin_kodas',
            field=models.CharField(max_length=20, verbose_name='VIN kodas'),
        ),
    ]