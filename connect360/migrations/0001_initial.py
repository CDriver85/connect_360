# Generated by Django 3.0.9 on 2020-08-06 16:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParentRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('address_1', models.CharField(blank=True, max_length=255, null=True)),
                ('address_2', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(default='Georgia', max_length=255)),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('phone', models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+9999999999'.", regex='^\\+?\\d{10}$')])),
                ('school', models.CharField(blank=True, max_length=255, null=True)),
                ('number_of_devices', models.CharField(blank=True, max_length=1, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
