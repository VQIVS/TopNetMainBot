# Generated by Django 4.1 on 2023-09-30 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0030_alter_user_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(max_length=255),
        ),
    ]
