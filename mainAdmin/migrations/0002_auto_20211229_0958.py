# Generated by Django 3.2.9 on 2021-12-29 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainAdmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=120)),
                ('user', models.TextField(max_length=120, null=True)),
                ('price', models.TextField(max_length=200)),
                ('total', models.IntegerField(default=0, null=True)),
                ('quantity', models.TextField(default=1, max_length=100, null=True)),
                ('qtyInSt', models.TextField(default=0, max_length=100, null=True)),
                ('description', models.TextField(max_length=500, null=True)),
                ('image', models.TextField(max_length=120, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='order',
            old_name='image',
            new_name='userName',
        ),
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]