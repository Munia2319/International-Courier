# Generated by Django 4.0 on 2022-06-14 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0007_order_details'),
    ]

    operations = [
        migrations.DeleteModel(
            name='order_detail',
        ),
    ]
