# Generated by Django 3.2.23 on 2024-01-14 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zena', '0002_new_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new',
            old_name='location',
            new_name='link',
        ),
        migrations.AddField(
            model_name='new',
            name='_from',
            field=models.CharField(default='', max_length=300),
        ),
    ]
