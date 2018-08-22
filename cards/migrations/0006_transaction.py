# Generated by Django 2.1 on 2018-08-22 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0005_auto_20180822_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('balance', 'Balance'), ('withdrawal', 'Withdrawal')], max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('cash_value', models.TextField(max_length=120)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.Card')),
            ],
        ),
    ]
