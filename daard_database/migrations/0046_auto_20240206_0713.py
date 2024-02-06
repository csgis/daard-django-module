# Generated by Django 2.2.28 on 2024-02-06 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daard_database', '0045_auto_20240125_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseasecase',
            name='age_class',
            field=models.CharField(choices=[('Fetus (until birth)', 'Fetus (until birth)'), ('Infans (0 – 3\xa0years)', 'Infans (0 – 3\xa0years)'), ('Infans (4 – 6\xa0years)', 'Infans (4 – 6\xa0years)'), ('Infans (7 – 12\xa0years)', 'Infans (7 – 12\xa0years)'), ('Adolescent (13 – 20\xa0years)', 'Adolescent (13 – 20\xa0years)'), ('Early Adult (21 – 35\xa0years)', 'Early Adult (21 – 35\xa0years)'), ('Late Adult (36 – 50\xa0years)', 'Late Adult (36 – 50\xa0years)'), ('Senile (50 +\xa0years)', 'Senile (50 +\xa0years)'), ('unknown', 'unknown')], max_length=200),
        ),
    ]