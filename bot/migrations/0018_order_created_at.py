# Generated by Django 4.1 on 2023-09-30 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0017_alter_order_link_id_alter_user_emails_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
