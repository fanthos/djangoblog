# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='uri',
            field=models.CharField(default='', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pages',
            name='title',
            field=models.CharField(default='new page', max_length=100),
            preserve_default=True,
        ),
    ]
