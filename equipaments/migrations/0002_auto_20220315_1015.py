# Generated by Django 2.2.6 on 2022-03-15 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipaments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boxs',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='Preço'),
        ),
        migrations.AddField(
            model_name='cables',
            name='priceForMetter',
            field=models.FloatField(blank=True, null=True, verbose_name='Preço'),
        ),
        migrations.AddField(
            model_name='spliters',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='Preço'),
        ),
    ]