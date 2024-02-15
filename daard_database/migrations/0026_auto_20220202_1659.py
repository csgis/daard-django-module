from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('daard_database', '0025_auto_20220202_1412'),
    ]

    operations = [
        migrations.RunSQL(
            """
            UPDATE daard_database_diseasecase
            SET storage_place = jsonb_build_object('value', storage_place::text)
            WHERE storage_place IS NOT NULL;
            """,
            """
            UPDATE daard_database_diseasecase
            SET storage_place = ('{"value":' || storage_place::text || '}')::jsonb
            WHERE storage_place IS NOT NULL;
            """
        ),
        migrations.AlterField(
            model_name='diseasecase',
            name='storage_place',
            field=models.JSONField(default=dict),
        ),
    ]
