# Generated by Django 2.0.6 on 2018-07-02 16:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0007_auto_20180630_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.Event')),
            ],
        ),
        migrations.AddField(
            model_name='renter',
            name='requests',
            field=models.CharField(max_length=1000, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
        migrations.AddField(
            model_name='request',
            name='renter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.Renter'),
        ),
    ]
