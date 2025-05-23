# Generated by Django 5.1.6 on 2025-04-20 20:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolarPanel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('panel_code', models.CharField(blank=True, max_length=20)),
                ('panel_energy', models.IntegerField()),
                ('panel_condition', models.CharField(blank=True, max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='SolarPlant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_code', models.CharField(blank=True, max_length=20)),
                ('plant_name', models.CharField(max_length=32)),
                ('plant_address', models.CharField(blank=True, max_length=128)),
                ('plant_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.member')),
                ('plant_panels', models.ManyToManyField(to='mainapp.solarpanel')),
            ],
        ),
    ]
