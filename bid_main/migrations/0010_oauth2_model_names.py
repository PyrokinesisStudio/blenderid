# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 15:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bid_main', '0009_oauth2_models'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='oauth2accesstoken',
            options={'verbose_name': 'OAuth2 access token'},
        ),
        migrations.AlterModelOptions(
            name='oauth2application',
            options={'verbose_name': 'OAuth2 application'},
        ),
        migrations.AlterModelOptions(
            name='oauth2refreshtoken',
            options={'verbose_name': 'OAuth2 refresh token'},
        ),
    ]