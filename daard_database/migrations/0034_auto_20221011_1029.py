# Generated by Django 2.2.20 on 2022-10-11 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daard_database', '0033_auto_20221011_1025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diseaselibrary',
            name='disease_alias',
        ),
        migrations.AddField(
            model_name='diseaselibrary',
            name='disease_alias',
            field=models.ManyToManyField(blank=True, related_name='aliasses', to='daard_database.DiseaseAlias'),
        ),
    ]
