# Generated by Django 3.1.7 on 2021-04-08 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('daard_database', '0039_auto_20210407_1231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diseasecase',
            old_name='bone_bx',
            new_name='bone_amount',
        ),
        migrations.RemoveField(
            model_name='diseasecase',
            name='bone_by',
        ),
        migrations.RemoveField(
            model_name='diseasecase',
            name='bone_bz',
        ),
        migrations.AlterField(
            model_name='diseasecase',
            name='disease',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anomalies_case', to='daard_database.diseaselibrary'),
        ),
    ]