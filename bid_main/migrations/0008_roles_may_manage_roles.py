# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 14:28
from __future__ import unicode_literals

from django.db import migrations, models

# Not sure why Django wants this migration, but it keeps popping up.
class Migration(migrations.Migration):

    dependencies = [
        ('bid_main', '0007_user_add_indices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='may_manage_roles',
            field=models.ManyToManyField(blank=True, help_text='Users with this role will be able to grant or revoke these roles to any other user.', related_name='managers', to='bid_main.Role'),
        ),
    ]
