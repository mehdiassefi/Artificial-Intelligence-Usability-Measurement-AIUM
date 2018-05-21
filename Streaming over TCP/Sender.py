import pyaudio
import socket
import sys
import time
import wave
import Tkinter 
po=Tkinter.Tk()
RECORD_SECONDS=15
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1

    
RATE = 10240
WAVE_OUTPUT_FILENAME = "out1.wav"
 
p = pyaudio.PyAudio()
counter=0
stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate=RATE,
                input = True,
                frames_per_buffer = CHUNK)

TCP_IP = '192.168.1.10'
TCP_PORT = 50000
BUFFER_SIZE = 4096
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
size = 1024
frames = []
sum = 0
while 1:
    data = stream.read(CHUNK)
    sum += len(data)
    print sum
    s.send(data)
    #s.recv(size)
def rec():
    print("* recording")
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data= stream.read(CHUNK)
        s.send(data)
        frames.append(data)
        print("* done recording")
def ex():
    sys.exit(0)
counter = 0 
def counter_label(label):
  counter = 0
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()
s.close()
stream.close()
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
