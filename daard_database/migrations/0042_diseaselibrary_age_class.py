# Generated by Django 3.1.7 on 2021-04-28 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daard_database', '0041_bonerelation'),
    ]

    operations = [
        migrations.AddField(
            model_name='diseaselibrary',
            name='age_class',
            field=models.CharField(choices=[('Foetus', 'Foetus'), ('0–3', '0 – 3'), ('4–6', '4 – 6'), ('7–12', '7 – 12'), ('13–20', '13 – 20'), ('21–35', '21 – 35'), ('36–50', '36 – 50'), ('50+', '50 +'), ('Unknown', 'Unknown')], default='Foetus', max_length=200),
            preserve_default=False,
        ),
    ]