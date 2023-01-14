# Generated by Django 4.1.5 on 2023-01-14 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_remove_customuser_is_consumer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Farmer'), (2, 'Consumer')], null=True),
        ),
    ]