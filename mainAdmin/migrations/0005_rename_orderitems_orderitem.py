# Generated by Django 3.2.9 on 2021-12-29 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainAdmin', '0004_rename_order_orderitems'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='orderItems',
            new_name='orderItem',
        ),
    ]