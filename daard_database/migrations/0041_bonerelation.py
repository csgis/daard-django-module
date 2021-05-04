# Generated by Django 3.1.7 on 2021-04-08 16:28

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('daard_database', '0040_auto_20210408_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoneRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anomalies_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anomalies_case', to='daard_database.diseasecase')),
                ('bone_case', mptt.fields.TreeManyToManyField(related_name='bone_proxy_case', to='daard_database.Bone')),
                ('bone_change_case', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bone_change_proxy_case', to='daard_database.bonechange')),
                ('technic_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='technic_proxy_case', to='daard_database.technic')),
            ],
        ),
    ]
