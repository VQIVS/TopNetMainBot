# Generated by Django 4.1 on 2023-09-29 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0013_email_rename_email_user_primary_email_remove_link_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='context',
            field=models.JSONField(default=dict),
        ),
    ]
