# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 14:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bid_main', '0006_role_is_public'),
    ]

    # See https://github.com/evonove/django-oauth-toolkit/issues/227#issuecomment-225836009
    run_before = [
        ('oauth2_provider', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OAuth2AccessToken',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('host_label', models.CharField(blank=True, max_length=255)),
                ('subclient', models.CharField(blank=True, max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('expires', models.DateTimeField()),
                ('scope', models.TextField(blank=True)),
                ('token', models.CharField(max_length=255, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bid_main_oauth2accesstoken', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'access token',
            },
        ),
    ]