from commands import COMMAND_CLASSES
from commands.base import BaseCommand
from core.context import AssistantContext

class Dispatcher:
    def __init__(self):
        self.commands = [cls() for cls in COMMAND_CLASSES if issubclass(cls, BaseCommand)]

    def process(self, text: str, ctx: AssistantContext) -> bool:
        """Ищет команду по триггерам и передаёт ей полный текст для анализа."""
        cleaned = text.lower().strip()
        for cmd in self.commands:
            # Проверяем, есть ли хоть один триггер команды в распознанной фразе
            if any(t in cleaned.split() for t in cmd.triggers):
                return cmd.execute(ctx, cleaned)
        return False