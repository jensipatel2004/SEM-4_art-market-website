# Generated by Django 5.1.1 on 2024-09-26 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_remove_customer_email_remove_customer_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='phone_number',
        ),
    ]
