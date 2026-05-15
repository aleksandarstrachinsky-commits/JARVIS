import os
import subprocess
import sys
from commands.base import BaseCommand
from core.context import AssistantContext
from config import TARGET_SCRIPT

class SystemCommand(BaseCommand):
    name = "system"
    triggers = ["запуск", "стоп", "выход"]

    def execute(self, ctx: AssistantContext, full_text: str) -> bool:
        words = full_text.split()

        # 🔹 ПРОВЕРКА СТОП
        if "стоп" in words or "выход" in words:
            print("🛑 Команда остановки распознана. Завершаю работу...")
            ctx.running = False
            return True

        # 🔹 ПРОВЕРКА ЗАПУСК
        if "запуск" in words:
            print("🚀 Выполняю запуск скрипта...")
            if os.path.exists(TARGET_SCRIPT):
                subprocess.Popen([sys.executable, TARGET_SCRIPT])
            else:
                print(f"❌ Файл не найден: {TARGET_SCRIPT}")
            return True

        return False