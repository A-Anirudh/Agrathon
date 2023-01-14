# Generated by Django 4.1.5 on 2023-01-14 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_customuser_is_consumer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_consumer',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_farmer',
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Farmer'), (2, 'Consumer')], default=1),
            preserve_default=False,
        ),
    ]