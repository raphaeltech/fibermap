# Generated by Django 2.2.6 on 2022-03-14 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipaments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='positionPoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification', models.CharField(max_length=256, verbose_name='Identificação')),
                ('geolocation', models.CharField(max_length=100, verbose_name='Geolocalização')),
                ('isLocate', models.BooleanField(blank=True, null=True, verbose_name='Alugado')),
                ('priceLocation', models.FloatField(blank=True, null=True, verbose_name='Valor da locação')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('poleModel', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='equipaments.poles', verbose_name='Modelo do Poste')),
            ],
        ),
        migrations.CreateModel(
            name='positionSteels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification', models.CharField(max_length=256, verbose_name='Identificação')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('modelSteel', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='equipaments.steels', verbose_name='Modelo da Ferragem')),
                ('poleIdentification', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inventory.positionPoles', verbose_name='Poste')),
            ],
        ),
        migrations.CreateModel(
            name='ctos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification', models.CharField(max_length=256, verbose_name='Identificação')),
                ('fusion', models.BooleanField(null=True, verbose_name='Existe Fusão?')),
                ('numberFusion', models.BigIntegerField(blank=True, null=True, verbose_name='Numero de fusões')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('ctoModel', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='equipaments.boxs', verbose_name='Modelo da CTO')),
                ('pole', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inventory.positionPoles', verbose_name='Poste')),
                ('spliter1', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spliter1', to='equipaments.spliters', verbose_name='Spliter 1')),
                ('spliter2', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spliter2', to='equipaments.spliters', verbose_name='Spliter 2')),
                ('spliter3', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spliter3', to='equipaments.spliters', verbose_name='Spliter 3')),
            ],
        ),
        migrations.CreateModel(
            name='ceos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification', models.CharField(max_length=256, verbose_name='Identificação')),
                ('numberTray', models.BigIntegerField(null=True, verbose_name='Numero de Bandeijas')),
                ('numberFusion', models.BigIntegerField(null=True, verbose_name='Numero de Fusões')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('ceoModel', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='equipaments.boxs', verbose_name='Modelo da CEO')),
                ('pole', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inventory.positionPoles', verbose_name='Poste')),
            ],
        ),
    ]