# Generated by Django 2.2 on 2020-11-23 11:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchingApp', '0005_auto_20201123_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matching',
            name='likers',
            field=models.ManyToManyField(blank=True, related_name='matching_likers', to=settings.AUTH_USER_MODEL, verbose_name='찜한 사용자'),
        ),
    ]
