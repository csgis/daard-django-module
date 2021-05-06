# Generated by Django 2.2.16 on 2021-05-06 14:17

from django.db import migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('daard_database', '0003_auto_20210506_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseasecase',
            name='position',
            field=geoposition.fields.GeopositionField(default=(0, 0), max_length=42),
            preserve_default=False,
        ),
    ]
