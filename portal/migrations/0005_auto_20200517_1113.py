# Generated by Django 3.0.6 on 2020-05-17 11:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_policy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='policy',
            options={'verbose_name_plural': 'policies'},
        ),
        migrations.RenameField(
            model_name='policy',
            old_name='product',
            new_name='products',
        ),
        migrations.AddField(
            model_name='policy',
            name='coverage_end',
            field=models.DateField(default=datetime.date(2021, 5, 17)),
        ),
        migrations.AddField(
            model_name='policy',
            name='coverage_start',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
