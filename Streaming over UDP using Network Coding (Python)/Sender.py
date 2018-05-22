import os
import sys
import pyaudio
import socket
import wave
import time
from threading import Thread
import pickle 
UDP_A = ''
group_no = 0 
class packet:
      def __init__(self):
            self.frames = []
            self.arr = []
            self.ord = 0
            self.group = 0
     
pkt0 = packet()
pkt1 = packet()
pkt2 = packet()
pkt3 = packet()
pkt4 = packet()
kp = packet()
playlist = []
test=[]
sample_list = []
flaglist = [0]
def charN(str, N):
    if N < len(str):
        return str[N]
    return 'X'
def xor(str1,str2):
    length = len(str1)
    return ''.join(chr(ord(charN(str2,i)) ^ ord(charN(str1,i)))     for i in xrange(length))
def _join(str):
    length = len(str)
    return ''.join(str.pop(0)     for i in xrange(length))

def sampl(stream, CHUNK):
      A = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
      group_no = 0      
      s = [1,1,1,1,1]
      x= [1,1,1,1,1]
      while True:
            #---------- Reading voice samples --------
            c0 = stream.read(CHUNK)
            c1 = stream.read(CHUNK)
            c2 = stream.read(CHUNK)
            c3 = stream.read(CHUNK)
            c4 = stream.read(CHUNK)
                                           #        Coding . . . 
            c=c0                           #0
            c = xor(c,c1)
            c = xor(c,c2)
            pkt0.frames.append(c)
            pkt0.arr = [1, 1, 1, 0, 0]
            c=c1                           #1
            c = xor(c,c2)
            c = xor(c,c3)
            pkt1.frames.append(c)
            pkt1.arr = [0, 1, 1, 1, 0]
            c=c2                           #2
            c = xor(c,c3)
            c = xor(c,c4)
            pkt2.frames.append(c)
            pkt2.arr = [0, 0, 1, 1, 1]
            c=c1                           #3
            c = xor(c,c2)
            c = xor(c,c4)
            pkt3.frames.append(c)
            pkt3.arr = [0, 1, 1, 0, 1]
            c=c1                           #4
            c = xor(c,c3)
            c = xor(c,c4)
            pkt4.frames.append(c)
            pkt4.arr = [0, 1, 0, 1, 1]
            A = [[1, 1, 1, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 1, 1], [0, 1, 1, 0, 1], [0, 1, 0, 1, 1]]
            
            pk0 = ''
            pk1 = ''
            pk2 = ''
            pk3 = ''
            pk4 = ''
            
            cal0 = []
            cal1 = []
            cal2 = []
            cal3 = []
            cal4 = []
            ccc0 = pkt0.frames.pop(0)
            ccc1 = pkt1.frames.pop(0)
            ccc2 = pkt2.frames.pop(0)
            ccc3 = pkt3.frames.pop(0)
            ccc4 = pkt4.frames.pop(0)
            length = len(ccc0)                    #       Decoding . . .
            for ii in range(0,length):
                  AA = A
                  s = [1,1,1,1,1]
                  A = [[1, 1, 1, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 1, 1], [0, 1, 1, 0, 1], [0, 1, 0, 1, 1]]
                  s[0] = ord(charN(ccc0,ii))
                  s[1] = ord(charN(ccc1,ii))
                  s[2] = ord(charN(ccc2,ii))
                  s[3] = ord(charN(ccc3,ii))
                  s[4] = ord(charN(ccc4,ii)) 
                  x = SolveLinearSystem (AA, s, 5)  #Solving each partial equatoin
                  cal0.append(chr(x[0]))        #Collecting partial solutions
                  cal1.append(chr(x[1]))
                  cal2.append(chr(x[2]))
                  cal3.append(chr(x[3]))
                  cal4.append(chr(x[4]))
            pk0 = _join(cal0)                   #joining partial solutions
            pk1 = _join(cal1)
            pk2 = _join(cal2)
            pk3 = _join(cal3)
            pk4 = _join(cal4) 
            playlist.append(pk0)                #Sending resulted packets to the playlist
            playlist.append(pk1)
            playlist.append(pk2)
            playlist.append(pk3)
            playlist.append(pk4)
                  
                  
            

def SolveLinearSystem (A, B, N):
    for K in range (0, N):
        if (A[K][K] == 0):
            for i in range (K+1, N):
                if (A[i][K]!=0):
                    for L in range (0, N):
                        s = A[K][L]
                        A[K][L] = A[i][L]
                        A[i][L] = s
                    s = B[i]
                    B[i] = B[K]
                    B[K] = s
                    break
        for I in range (0, N):
            if (I!=K):
                if (A[I][K]):
                    #M = 0
                    for M in range (K, N):
                        A[I][M] = A[I][M] ^ A[K][M]
                    B[I] = B[I] ^ B[K]
    
    #print "After", B
    return B

def s_read():                                #add raw voice samples to a list to be processed
      while True:
            c = stream.read(CHUNK)        
            sample_list.append(c)
      #print len(sample_list)
      
def ply():
      played_no = 0
      while True: 
            if len(playlist)>0 :
                  pk = playlist.pop(0)
                  udp.sendto(pk, ("127.0.0.1", 5000))
      
if __name__ == "__main__":
      CHUNK = 512
      FORMAT = pyaudio.paInt16
      CHANNELS = 1
      RATE = 10240
      p = pyaudio.PyAudio()
      stream = p.open(format = FORMAT,
                      channels = CHANNELS,
                      rate = RATE,
                      input = True,
                      frames_per_buffer = CHUNK,
                      )
      udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      Ts = Thread(target = sampl, args=(stream, CHUNK,))
      Tp = Thread(target = ply)
      Ts.setDaemon(True)
      Tp.setDaemon(True)
      Ts.start()
      Tp.start()
      Ts.join()
      Tp.join()
      udp.close()
      
      
