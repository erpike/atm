# Generated by Django 2.1 on 2018-08-21 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='number',
            field=models.TextField(max_length=16),
        ),
    ]