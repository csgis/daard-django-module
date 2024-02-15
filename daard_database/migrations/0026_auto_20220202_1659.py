from django.db import migrations, models
from django.db.migrations.operations.special import RunSQL

class Migration(migrations.Migration):

    dependencies = [
        ('daard_database', '0025_auto_20220202_1412'),
    ]

    operations = [
        RunSQL(
            "ALTER TABLE daard_database_diseasecase ALTER COLUMN storage_place TYPE jsonb USING storage_place::text::jsonb",
            reverse_sql="ALTER TABLE daard_database_diseasecase ALTER COLUMN storage_place TYPE integer USING storage_place::text::integer"
        ),
    ]
