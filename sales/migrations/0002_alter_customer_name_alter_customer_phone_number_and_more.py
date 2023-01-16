# Generated by Django 4.1.5 on 2023-01-15 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]