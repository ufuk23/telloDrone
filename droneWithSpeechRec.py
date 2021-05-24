import json
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer, SetLogLevel

q = queue.Queue()


def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    q.put(bytes(indata))


try:
    device_info = sd.query_devices(0, 'input')
    samplerate = int(device_info['default_samplerate'])

    model = Model("model-tr")

    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=0,
                           dtype='int16', channels=1, callback=callback):

        print('Press Ctrl+C to stop the recording')

        rec = KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                res = json.loads(rec.Result())
                print(res['text'])

except Exception as e:
    print(type(e).__name__ + ': ' + str(e))
