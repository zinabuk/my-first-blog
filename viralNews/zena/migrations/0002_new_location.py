# Generated by Django 3.2.23 on 2024-01-14 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zena', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='location',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
