import re

def clean_text(text: str) -> str:
    """Нормализация: нижний регистр, удаление пунктуации, схлопывание пробелов."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s]', '', text)
    return " ".join(text.split())