# Generated by Django 4.1 on 2023-09-30 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0031_alter_user_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
