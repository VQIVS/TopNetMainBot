# Generated by Django 4.2.4 on 2023-09-17 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_user_purchase_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
