# Generated by Django 3.1.7 on 2021-03-29 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daard_database', '0012_auto_20210329_0835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formconfig',
            old_name='values',
            new_name='config',
        ),
    ]