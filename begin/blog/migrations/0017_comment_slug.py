# Generated by Django 2.2.3 on 2019-07-29 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_remove_comment_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='slug',
            field=models.SlugField(default=True),
        ),
    ]
