# Generated by Django 5.1.1 on 2024-09-22 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_order_complete_alter_product_digital_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='digital',
        ),
    ]
