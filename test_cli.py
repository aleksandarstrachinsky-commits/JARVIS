import sys
import traceback
from core.dispatcher import Dispatcher
from core.context import AssistantContext

class CommandTester:
    def __init__(self):
        self.ctx = AssistantContext()
        self.dispatcher = Dispatcher()
        self.history = []

    def run(self):
        print("="*60)
        print("🧪 КОНСОЛЬНЫЙ ТЕСТЕР КОМАНД")
        print("Вводите фразы. Для завершения: 'стоп' / 'выход' / Ctrl+C")
        print("Совет: тестируйте команды БЕЗ слова 'Джарвис' (диспетчер принимает только тело команды)")
        print("="*60 + "\n")

        while self.ctx.running:
            try:
                raw = input("🗣️ Вы: ").strip()
                if not raw:
                    continue

                if raw.lower() in ("стоп", "выход", "exit", "quit"):
                    print("🛑 Завершение сессии...")
                    self.ctx.running = False
                    break

                self.history.append({"input": raw})
                print(f"\n📤 Отправка в Dispatcher: '{raw}'")

                # 🔍 Выполнение через диспетчер
                success = self.dispatcher.process(raw, self.ctx)

                if success:
                    print("✅ Команда найдена и выполнена.")
                else:
                    print("⚠️ Триггер не распознан. Фраза проигнорирована.")

                # 📊 Диагностика состояния
                print(f"📊 Context: running={self.ctx.running} | last_cmd='{self.ctx.last_command}'")
                print("─" * 60)

            except KeyboardInterrupt:
                print("\n⚠️ Прервано пользователем.")
                self.ctx.running = False
                break
            except Exception as e:
                print(f"❌ Критическая ошибка в команде: {e}")
                traceback.print_exc()
                print("💡 Совет: команда не должна ломать диспетчер. Оберните логику в try/except.")
                print("─" * 60)

        self._show_summary()

    def _show_summary(self):
        print("\n📜 ИСТОРИЯ СЕССИИ:")
        for i, rec in enumerate(self.history, 1):
            print(f"{i}. {rec['input']}")
        print(f"\n📝 Записей в транскрипции: {len(self.ctx.transcript)}")
        print("🏁 Тест завершен.")

if __name__ == "__main__":
    tester = CommandTester()
    tester.run()