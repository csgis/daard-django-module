# Generated by Django 2.2.20 on 2022-01-31 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daard_database', '0015_auto_20220131_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseasecase',
            name='references',
            field=models.TextField(blank=True, null=True),
        ),
    ]
