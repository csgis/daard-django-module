# Generated by Django 2.2.20 on 2022-01-31 13:41

import daard_database.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daard_database', '0023_auto_20220131_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helper',
            name='pdf',
            field=models.FileField(help_text='Name must be daard_help.pdf', storage=daard_database.storage.OverwriteStorage(), upload_to='pdfs/'),
        ),
    ]