# Generated by Django 2.2.20 on 2022-01-31 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daard_database', '0020_auto_20220131_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Helps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('pdf', models.FileField(upload_to='pdfs/')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
