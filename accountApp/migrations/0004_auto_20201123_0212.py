# Generated by Django 2.2 on 2020-11-22 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accountApp', '0003_customer_mailing_assignment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='mailing_assignment',
            new_name='mailing_agreement',
        ),
    ]
