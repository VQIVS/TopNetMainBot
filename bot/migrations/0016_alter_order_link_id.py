# Generated by Django 4.1 on 2023-09-29 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0015_remove_email_context_alter_user_emails_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='link_id',
            field=models.CharField(max_length=255),
        ),
    ]
