# Generated by Django 3.0.6 on 2020-05-21 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_ticket'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='filinguser',
            new_name='filing_user',
        ),
    ]
