# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-02 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perma_payments', '0004_subscriptionrequestresponse_encryption_key_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionrequestresponse',
            name='full_response',
            field=models.BinaryField(help_text='The full response, encrypted, in case we ever need it.'),
        ),
    ]
