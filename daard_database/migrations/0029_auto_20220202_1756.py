# Generated by Django 2.2.20 on 2022-02-02 17:56

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('daard_database', '0028_auto_20220202_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseasecase',
            name='dating_method',
            field=jsonfield.fields.JSONField(blank=True, default=list, null=True),
        ),
    ]
