import pyaudio
import socket
import sys
from threading import Thread
UDP_A = ''
frames = []

def udpStream(udp, CHUNK):

    sum1 = 0
    while True:
        soundData, addr = udp.recvfrom(CHUNK)
        sum1 += len(soundData)
	#print "receive : ", sum1
	frames.append(soundData)

def play(stream, CHUNK):
    BUFFER = 10
    while True:
            if len(frames) > 1: 
                #while True:
		a = frames.pop(0)
                stream.write(a)

if __name__ == "__main__":
    FORMAT = pyaudio.paInt16
    CHUNK = 2048   
    CHANNELS = 1
    RATE = 10240

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    output = True,
			)
                    #frames_per_buffer = CHUNK,
                    #)

    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind((UDP_A, 5000))

    Ts = Thread(target = udpStream, args=(udp, CHUNK,))
    Tp = Thread(target = play, args=(stream, CHUNK,))
    Ts.setDaemon(True)
    Tp.setDaemon(True)
    Ts.start()
    Tp.start()
    Ts.join()
    Tp.join()

    udp.close()