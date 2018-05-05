import pyaudio
import numpy as np
from threading import Thread
import calendar
import time

def handler(*data):
    for i in data:
        for j in i:
            print(j)

# edited from this link
# https://gist.github.com/mabdrabo/8678538

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
BITS_PER_LETTER = 3
BIT_RECORD_SECONDS = 4
WAVE_OUTPUT_FILENAME = "file.wav"

audio = pyaudio.PyAudio()

stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)

while(1):
    future =  calendar.timegm(time.gmtime()) + 16
    frames = []
    data = []
    for i in range(0, BITS_PER_LETTER):
        for i in range(0, int(RATE / CHUNK * BIT_RECORD_SECONDS)):
            frames.append(stream.read(CHUNK))

    for i in frames:
        frame = []
        for j in i:
            frame.append(ord(j))
        data.append(frame)
    data = np.array(data)
    Thread(target=handler, args=(data)).start()
    curr_time =  calendar.timegm(time.gmtime())
    #print("CURR_TIME: " + str(curr_time))
    #print("FUTURE: " + str(future))
    #print(future - curr_time)
    time.sleep((future - curr_time))
    #print("LOOP")

# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
