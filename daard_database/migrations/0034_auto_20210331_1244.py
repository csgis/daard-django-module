# Generated by Django 3.1.7 on 2021-03-31 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daard_database', '0033_diseasecase_bone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseasecase',
            name='age_freetext',
            field=models.CharField(max_length=200),
        ),
    ]