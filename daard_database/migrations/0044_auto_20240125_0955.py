# Generated by Django 2.2.28 on 2024-01-25 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daard_database', '0043_auto_20240125_0943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diseasecase',
            name='narrower_age_class_freetext',
        ),
        migrations.AlterField(
            model_name='diseasecase',
            name='age_freetext',
            field=models.CharField(blank=True, help_text='Narrower age class freetext', max_length=200),
        ),
    ]
