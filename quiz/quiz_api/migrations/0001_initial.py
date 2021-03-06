# Generated by Django 2.2.10 on 2020-08-03 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='username')),
                ('rating', models.FloatField(default=0.0, verbose_name='rating')),
                ('bio', models.CharField(blank=True, max_length=256, verbose_name='about')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='', verbose_name='avatar')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
