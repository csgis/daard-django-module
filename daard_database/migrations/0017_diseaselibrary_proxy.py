# Generated by Django 3.1.7 on 2021-03-29 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daard_database', '0016_auto_20210329_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='diseaselibrary',
            name='proxy',
            field=models.ManyToManyField(to='daard_database.BoneChangeBoneProxy'),
        ),
    ]