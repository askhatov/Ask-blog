# Generated by Django 2.2.3 on 2019-10-27 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_account_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='address_one',
        ),
        migrations.RemoveField(
            model_name='account',
            name='address_two',
        ),
        migrations.RemoveField(
            model_name='account',
            name='city',
        ),
        migrations.RemoveField(
            model_name='account',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='account',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='account',
            name='name',
        ),
        migrations.RemoveField(
            model_name='account',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='account',
            name='state',
        ),
    ]
