# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0002_auto_20150126_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='text_html',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
