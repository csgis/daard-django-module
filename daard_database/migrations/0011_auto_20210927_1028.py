# Generated by Django 2.2.20 on 2021-09-27 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daard_database', '0010_bone_svgid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseasecase',
            name='publication_link',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]