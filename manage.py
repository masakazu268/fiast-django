#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
from pathlib import Path
import os
import sys
import dotenv  # ← 追加


def main():
    """Run administrative tasks."""
   # .env ファイルの絶対パスを指定して強制的によみこむ
    env_path = Path(__file__).resolve().parent / '.env'
    dotenv.load_dotenv(dotenv_path=env_path)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
