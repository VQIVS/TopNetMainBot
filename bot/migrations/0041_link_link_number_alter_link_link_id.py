# Generated by Django 4.1 on 2023-09-30 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0040_alter_link_link_id_alter_order_link_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='link_number',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='link',
            name='link_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
