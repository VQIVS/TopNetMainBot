# Generated by Django 4.1 on 2023-09-30 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0033_alter_order_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user_id',
            new_name='user_name',
        ),
    ]
