# Generated by Django 4.1 on 2023-09-30 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0038_alter_order_id_alter_user_id_alter_user_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='username',
            field=models.CharField(default='name', max_length=255),
        ),
    ]
