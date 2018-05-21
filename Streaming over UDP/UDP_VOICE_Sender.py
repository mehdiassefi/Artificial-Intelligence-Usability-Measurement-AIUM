import pyaudio
import socket
import wave
import time
from threading import Thread

frames = []
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 10240
p = pyaudio.PyAudio()
stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                )

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sum = 0
while True:
    c = stream.read(CHUNK)
    sum += len(c)
    print sum
    frames.append(c)
    if len(frames) > 0:
        udp.sendto(frames.pop(0), ("127.0.0.1", 5000))
        time.sleep(0.1)
 

  
