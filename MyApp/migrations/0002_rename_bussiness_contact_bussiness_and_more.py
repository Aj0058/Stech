# Generated by Django 4.2.2 on 2024-06-21 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Bussiness',
            new_name='bussiness',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Service',
            new_name='service',
        ),
    ]
