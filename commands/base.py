from abc import ABC, abstractmethod
from core.context import AssistantContext

class BaseCommand(ABC):
    """Контракт для всех плагинов команд."""
    @property
    @abstractmethod
    def name(self) -> str: ...

    @property
    @abstractmethod
    def triggers(self) -> list[str]: ...

    @abstractmethod
    def execute(self, ctx: AssistantContext, params: str) -> bool:
        """Возвращает True, если команда успешно обработана."""
        ...