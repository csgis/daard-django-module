# Generated by Django 3.1.7 on 2021-03-30 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daard_database', '0022_auto_20210330_0917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diseaselibrary',
            name='bone_change',
        ),
        migrations.RemoveField(
            model_name='diseaselibrary',
            name='technic',
        ),
    ]