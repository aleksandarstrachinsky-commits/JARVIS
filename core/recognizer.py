import vosk
import json
from config import MODEL_PATH, SAMPLE_RATE

class SpeechRecognizer:
    def __init__(self):
        model = vosk.Model(MODEL_PATH)
        self.rec = vosk.KaldiRecognizer(model, SAMPLE_RATE)

    def accept_waveform(self, audio_bytes: bytes) -> bool:
        return self.rec.AcceptWaveform(audio_bytes)

    def get_result(self) -> str:
        return json.loads(self.rec.Result()).get("text", "")

    def get_partial(self) -> str:
        return json.loads(self.rec.PartialResult()).get("partial", "")

    def get_final(self) -> str:
        return json.loads(self.rec.FinalResult()).get("text", "")