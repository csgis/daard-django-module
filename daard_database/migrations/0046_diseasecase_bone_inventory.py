# Generated by Django 3.1.7 on 2021-05-04 07:25

from django.db import migrations, models
from jsonfield import JSONField

class Migration(migrations.Migration):

    dependencies = [
        ('daard_database', '0045_auto_20210504_0718'),
    ]

    operations = [
        migrations.AddField(
            model_name='diseasecase',
            name='bone_inventory',
            field=JSONField(default={}),
            preserve_default=False,
        ),
    ]
