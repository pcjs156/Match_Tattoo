# Generated by Django 2.2 on 2020-12-01 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountApp', '0005_auto_20201123_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='kakao_code',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='카카오톡 고유 ID'),
        ),
    ]
