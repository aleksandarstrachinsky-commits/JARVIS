import sys
import os

def get_app_dir() -> str:
    """Папка, где лежит .exe (или скрипт). Для пользовательских файлов и логов."""
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def get_bundle_path(relative: str) -> str:
    """Путь к файлам внутри архива PyInstaller (модели, ассеты, код)."""
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", relative))