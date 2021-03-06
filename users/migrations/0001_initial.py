# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-12 21:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OpenHumansMember',
            fields=[
                ('oh_id', models.CharField(max_length=16, primary_key=True, serialize=False, unique=True)),
                ('access_token', models.CharField(max_length=256)),
                ('refresh_token', models.CharField(max_length=256)),
                ('token_expires', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
