# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 14:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


# This migration must be executed after the oauth2_provider.Application one,
# but the rest of our custom OAuth2AccessToken class must be migrated into
# the DB before that.
class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.OAUTH2_PROVIDER_APPLICATION_MODEL),
        ('bid_main', '0007_oauth2_tokens'),
    ]

    operations = [
        migrations.AddField(
            model_name='oauth2accesstoken',
            name='application',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.OAUTH2_PROVIDER_APPLICATION_MODEL),
        ),
    ]