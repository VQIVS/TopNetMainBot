# Generated by Django 4.1 on 2023-09-29 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0012_alter_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.EmailField(max_length=255, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='primary_email',
        ),
        migrations.RemoveField(
            model_name='link',
            name='id',
        ),
        migrations.AlterField(
            model_name='link',
            name='link_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AddField(
            model_name='user',
            name='emails',
            field=models.ManyToManyField(blank=True, to='bot.email'),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_by_email', to='bot.email'),
        ),
    ]
