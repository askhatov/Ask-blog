# Generated by Django 2.2.3 on 2019-08-01 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='publish_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
