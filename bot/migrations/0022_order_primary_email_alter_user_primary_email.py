# Generated by Django 4.1 on 2023-09-30 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0021_alter_order_created_at_alter_user_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='primary_email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary_email_order', to='bot.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='primary_email',
            field=models.EmailField(blank=True, max_length=255, unique=True),
        ),
    ]