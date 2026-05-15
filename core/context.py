class AssistantContext:
    """Единый объект состояния. Передаётся в команды, изолирует данные."""
    def __init__(self):
        self.running = True
        self.state = "idle"          # "idle" | "listening"
        self.command_buffer = []     # Буфер фраз после wake-word (для записи команд)
        self.transcript = []         # История обычной речи
        self.last_command = ""       # Последняя выполненная команда