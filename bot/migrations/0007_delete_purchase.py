# Generated by Django 4.1 on 2023-09-29 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0006_alter_order_link_id_alter_order_user_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Purchase',
        ),
    ]
