# 🔹 Явная регистрация команд. PyInstaller гарантированно увидит эти импорты.
from .system import SystemCommand

# Добавляй новые команды сюда:
# from .browser import BrowserCommand

COMMAND_CLASSES = [SystemCommand]