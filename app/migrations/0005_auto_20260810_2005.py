from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    # admin ユーザーが存在しない場合のみ作成
    if not User.objects.filter(username='admin').exists():
        User.objects.create(
            username='admin',
            email='admin@example.com',
            password=make_password('admin1234'),  # ← 仮のパスワード（後で変更できます）
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )

def reverse_func(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20260805_0200'),  # ※自動記述された直前のマイグレーション名のままでOK
    ]

    operations = [
        migrations.RunPython(create_superuser, reverse_func),
    ]