# Generated by Django 3.1.7 on 2021-03-29 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daard_database', '0007_diseaselibrary_technic'),
    ]

    operations = [
        migrations.AddField(
            model_name='diseaselibrary',
            name='bone_change',
            field=models.ManyToManyField(through='daard_database.BoneChangeBoneProxy', to='daard_database.BoneChange'),
        ),
    ]
