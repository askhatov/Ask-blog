# Generated by Django 2.2.3 on 2019-07-30 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20190729_2339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='slug',
        ),
    ]
