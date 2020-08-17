# Generated by Django 2.2.15 on 2020-08-17 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perma_payments', '0001_squashed_0017_purchaserequest_purchaserequestresponse'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='changerequest',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='changerequestresponse',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='outgoingtransaction',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='purchaserequestresponse',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='response',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='subscriptionrequest',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='subscriptionrequestresponse',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='updaterequest',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='updaterequestresponse',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterField(
            model_name='historicalsubscriptionagreement',
            name='created_date',
            field=models.DateTimeField(blank=True, editable=False),
        ),
        migrations.AlterField(
            model_name='historicalsubscriptionagreement',
            name='customer_type',
            field=models.CharField(choices=[('Registrar', 'Registrar'), ('Individual', 'Individual')], max_length=20),
        ),
    ]
