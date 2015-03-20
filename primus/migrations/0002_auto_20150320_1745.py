# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('primus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='contest',
            field=models.ForeignKey(to='primus.Contest', related_name='results'),
            preserve_default=True,
        ),
    ]
