# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-28 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("orgs", "0039_auto_20180202_1234"), ("msgs", "0118_auto_20180524_1826")]

    operations = [
        migrations.AddField(
            model_name="labelcount",
            name="is_archived",
            field=models.BooleanField(default=False, help_text="Whether this count is for archived messages"),
        ),
        migrations.AddField(
            model_name="systemlabelcount",
            name="is_archived",
            field=models.BooleanField(default=False, help_text="Whether this count is for archived messages"),
        ),
    ]