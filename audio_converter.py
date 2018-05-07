import pyaudio
import numpy as np
from threading import Thread
import calendar
import time
import decoder

def handler(*data):
    decoder.decode(data)
    for i in data:
        for j in i:
            print(j)

# edited from this link
# https://gist.github.com/mabdrabo/8678538

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
BITS_PER_TICK = 3
BIT_RECORD_SECONDS = 8

audio = pyaudio.PyAudio()

stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)

while(1):
    future =  calendar.timegm(time.gmtime()) + 4*(BIT_RECORD_SECONDS)
    frames = []
    data = []
    for i in range(0, BITS_PER_TICK):
        frame = []
        for j in range(0, int(RATE / CHUNK * BIT_RECORD_SECONDS)):
            frame.append(stream.read(CHUNK))
        frames.append(frame)

    frame = []
    for i in frames:
        frame = []
        for k in i:
            for j in k:
                frame.append(float(ord(j)))
        data.append(frame)
    data = np.array(data)
    Thread(target=handler, args=data).start()
    curr_time =  calendar.timegm(time.gmtime())
    time.sleep((future - curr_time))

# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
