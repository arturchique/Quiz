# Generated by Django 2.2.10 on 2020-08-06 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='name',
            new_name='nickname',
        ),
    ]
