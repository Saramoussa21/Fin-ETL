# Generated by Django 5.1.2 on 2024-10-19 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='transaction',
            name='transaction_date_idx',
        ),
    ]
