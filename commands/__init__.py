# 🔹 Явная регистрация команд. PyInstaller гарантированно увидит эти импорты.
from .system import SystemCommand
#from .browse import BrowserCommand

# Добавляй новые команды сюда:
# from .browser import BrowserCommand

COMMAND_CLASSES = [
    SystemCommand,
   # BrowserCommand,
    ]