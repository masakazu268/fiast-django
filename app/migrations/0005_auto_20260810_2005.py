from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_or_update_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    # admin ユーザーを取得（無ければ新規作成）
    user, created = User.objects.get_or_create(username='admin')
    
    # パスワードと権限を確実にセットして保存
    user.email = 'admin@example.com'
    user.password = make_password('admin1234')  # 強制的に admin1234 にセット
    user.is_staff = True                       # 管理画面ログイン権限
    user.is_superuser = True                   # 全権限
    user.is_active = True
    user.save()

def reverse_func(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_post_category'),  # ※ご自身の0004番のファイル名
    ]

    operations = [
        migrations.RunPython(create_or_update_superuser, reverse_func),
    ]