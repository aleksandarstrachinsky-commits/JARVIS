from utils.paths import get_app_dir, get_bundle_path
import os

# 🔊 Аудио
SAMPLE_RATE = 16000
CHUNK_SIZE = 4096

# 🎙️ Распознавание
MODEL_PATH = get_bundle_path("models/model-ru-small")
WAKE_WORD = "джарвис"

# 📁 Папки и файлы (всегда рядом с .exe)
APP_DIR = get_app_dir()
OUTPUT_FILE = os.path.join(APP_DIR, "transcription.txt")
TARGET_SCRIPT = os.path.join(APP_DIR, "tk_all.py")  # Положи этот скрипт рядом с .exe