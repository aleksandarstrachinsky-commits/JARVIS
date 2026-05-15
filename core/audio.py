import sounddevice as sd
from config import SAMPLE_RATE, CHUNK_SIZE

class AudioStream:
    def __init__(self):
        self.stream = sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype='int16',
            blocksize=CHUNK_SIZE
        )

    def start(self):
        self.stream.start()

    def stop(self):
        self.stream.stop()
        self.stream.close()

    def read(self) -> bytes:
        chunk, _ = self.stream.read(CHUNK_SIZE)
        return chunk.tobytes()