# Generated by Django 2.2.20 on 2022-10-11 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daard_database', '0032_auto_20221011_1006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diseaselibrary',
            name='disease_alias',
        ),
        migrations.AddField(
            model_name='diseaselibrary',
            name='disease_alias',
            field=models.ForeignKey(blank=True, null=True, on_delete='CASCADE', related_name='aliasses', to='daard_database.DiseaseAlias'),
        ),
    ]
