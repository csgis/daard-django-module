# Generated by Django 3.1.7 on 2021-05-04 07:27

from django.db import migrations, models
from jsonfield import JSONField

class Migration(migrations.Migration):

    dependencies = [
        ('daard_database', '0046_diseasecase_bone_inventory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diseasecase',
            name='bone',
        ),
        migrations.RemoveField(
            model_name='diseasecase',
            name='bone_amount',
        ),
        migrations.AddField(
            model_name='diseasecase',
            name='bone_relations',
            field=JSONField(default={}),
            preserve_default=False,
        ),
    ]