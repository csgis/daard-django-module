# Generated by Django 2.2.20 on 2021-07-20 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daard_database', '0007_auto_20210715_0814'),
    ]

    operations = [
        migrations.AddField(
            model_name='diseasecase',
            name='geoserver_id',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]