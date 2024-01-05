# Generated by Django 4.1.1 on 2024-01-05 17:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_tracker_amount_tracker_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='amount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='date',
            field=models.DateField(default=datetime.date(2024, 1, 5)),
        ),
    ]
