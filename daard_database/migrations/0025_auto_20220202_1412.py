# Generated by Django 2.2.20 on 2022-02-02 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('daard_database', '0024_auto_20220131_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseasecase',
            name='storage_place',
            field=models.ForeignKey(db_column='storage_place', null=True, on_delete=django.db.models.deletion.SET_NULL, to='daard_database.InstitutList'),
        ),
    ]
