# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-07 15:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamelibrary', '0007_release'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameRelease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('info', models.CharField(max_length=256)),
            ],
        ),
        migrations.DeleteModel(
            name='Release',
        ),
        migrations.AlterField(
            model_name='game',
            name='genres',
            field=models.ManyToManyField(blank=True, related_name='related_games', to='gamelibrary.GameGenre', verbose_name='Genre(s)'),
        ),
        migrations.AddField(
            model_name='gamerelease',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='releases', to='gamelibrary.Game'),
        ),
    ]
