import msvcrt
import sys
from core.audio import AudioStream
from core.recognizer import SpeechRecognizer
from core.context import AssistantContext
from core.dispatcher import Dispatcher
from config import OUTPUT_FILE
from utils.text import clean_text

def main():
    ctx = AssistantContext()
    audio = AudioStream()
    recognizer = SpeechRecognizer()
    dispatcher = Dispatcher()

    audio.start()
    print("✅ Готово! Скажите 'Джарвис', затем команду.")
    print("   ⏹️ Нажмите 'P' или скажите 'стоп' для остановки.\n")

    try:
        while ctx.running:
            # 🔑 Неблокирующая проверка клавиши (только Windows)
            if msvcrt.kbhit() and msvcrt.getch() in (b'p', b'P'):
                ctx.running = False
                break

            audio_bytes = audio.read()

            if recognizer.accept_waveform(audio_bytes):
                phrase = recognizer.get_result()
                if phrase:
                    if ctx.state == "idle":
                        if "джарвис" in clean_text(phrase).split():
                            ctx.state = "listening"
                            parts = phrase.lower().split("джарвис", 1)
                            cmd_part = parts[1].strip() if len(parts) > 1 else ""
                            ctx.command_buffer = [cmd_part] if cmd_part else []
                            print("\n🎙️ Джарвис слушает...")

                                # 🔧 ФИКС: Если команда шла сразу за wake-word в той же фразе — выполняем сразу
                            if cmd_part:
                                print(f"\n📝 Команда: '{cmd_part}'")
                                dispatcher.process(cmd_part, ctx)
                                ctx.command_buffer = []
                                ctx.state = "idle"
                        else:
                            ctx.transcript.append(phrase)
                            sys.stdout.write("\r" + " " * 80 + "\r")
                            print(f"✅ {phrase}")
                    else:
                        ctx.command_buffer.append(phrase.strip())
                        full_cmd = " ".join(ctx.command_buffer).strip()
                        print(f"\n📝 Команда принята: '{full_cmd}'")
                        dispatcher.process(full_cmd, ctx)
                        ctx.command_buffer = []
                        ctx.state = "idle"
            else:
                partial = recognizer.get_partial()
                if partial:
                    sys.stdout.write(f"\r🔄 {partial}" + " " * 60)
                    sys.stdout.flush()

    except KeyboardInterrupt:
        print("\n⚠️ Экстренный выход")
    finally:
        audio.stop()
        
        # Обработка "хвоста" после остановки
        final = recognizer.get_final()
        if final:
            if ctx.state == "listening":
                ctx.command_buffer.append(final.strip())
                dispatcher.process(" ".join(ctx.command_buffer).strip(), ctx)
            else:
                ctx.transcript.append(final)

        if ctx.transcript:
            with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
                f.write("\n".join(ctx.transcript))
            print(f"\n💾 Текст сохранён: {OUTPUT_FILE}")
        print("📦 Сессия завершена.")

if __name__ == "__main__":
    main()