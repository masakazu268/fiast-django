from django.db import migrations

def fix_category_sequence(apps, schema_editor):
    # PostgreSQL の場合のみ、ID の自動採番カウンターを現在の最大値に修正する
    if schema_editor.connection.vendor == 'postgresql':
        with schema_editor.connection.cursor() as cursor:
            cursor.execute(
                "SELECT setval(pg_get_serial_sequence('app_category', 'id'), COALESCE(MAX(id), 1)) FROM app_category;"
            )

def reverse_func(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20260810_2005'),  # ※ご自身の 0005 番のマイグレーションファイル名
    ]

    operations = [
        migrations.RunPython(fix_category_sequence, reverse_func),
    ]