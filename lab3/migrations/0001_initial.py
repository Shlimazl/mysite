# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-31 19:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='airlines',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='departure',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=1000)),
                ('country', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='destination',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=1000)),
                ('country', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='flights',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('departure_time', models.CharField(max_length=1000)),
                ('airlines_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airline', to='lab3.airlines')),
                ('departure_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure', to='lab3.departure')),
                ('destination_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='lab3.destination')),
            ],
        ),
        migrations.CreateModel(
            name='planes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=1000)),
                ('type', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='flights',
            name='plane_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plane', to='lab3.planes'),
        ),
    ]
