# Generated by Django 4.2.2 on 2024-06-21 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_rename_bussiness_contact_business'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='business',
            new_name='Business',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='message',
            new_name='Message',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='phone',
            new_name='Phone',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='service',
            new_name='Service',
        ),
    ]
