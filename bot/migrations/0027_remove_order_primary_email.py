# Generated by Django 4.1 on 2023-09-30 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0026_alter_order_primary_email_alter_user_primary_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='primary_email',
        ),
    ]