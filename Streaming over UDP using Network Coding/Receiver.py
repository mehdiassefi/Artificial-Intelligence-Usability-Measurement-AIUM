import pyaudio
import socket
import pickle
import sys
import datetime
from threading import Thread
UDP_A = ''
frams = []
playlist = []
flags = []
xors = []
coef = []
arr1 = []
groups = []
A = [[0 for x in xrange(5)]for x in xrange(5)]
AA= [[0 for x in xrange(5)]for x in xrange(5)]
s = []
_ord = 0
_ccc = []
class packet:
    def __init__(self):
        self.frames = []
        self.arr = []
        self.group = 0
class coeficients:
    def __init__(self):
        self.co = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
_coe1 = coeficients()
_coe2 = coeficients()
pkt = packet()

def udpStream(udp, CHUNK):
    
    while True:        
        soundData, addr = udp.recvfrom(CHUNK)
        pkt = pickle.loads(soundData)
        coe = pkt.arr
        grp = pkt.group
        if coef.count(grp)<5:
            xors.append(pkt.frames.pop(0))
            groups.append(grp)
            coef.append(arrtoint(coe))
            #print coef
        else:
            pkt.frames.pop(0)



def extract():
    cnt = 0         # Number of packets that have been arrived for the current group
    cur = 0         # Current group number
    nw = 1          # New group of packets is about to be read
    p0 = ''         # Final calculated packets to send to the playlist
    p1 = ''
    p2 = ''
    p3 = ''
    p4 = ''
    cal0 = []       # Final calculated packets to be joined together
    cal1 = []
    cal2 = []
    cal3 = []
    cal4 = []
    flg0 = 0
    flg1 = 0
    flg2 = 0
    flg3 = 0
    flg4 = 0
    flg5 = 0
    flg6 = 0
    solved = 0 
    
    while True:
        if len(xors) > 1:        
            _groups = groups.pop(0)
            _coef = coef.pop(0)
            _xors = xors.pop(0)            
            if nw == 1:
                nw =0
                cur = _groups
            if cnt < 6 :
                if _coef == 7:
                    A0 = inttoarr(_coef)
                    _ccc0 = _xors
                    flg0 = 1
                    cnt = cnt +1
                elif _coef == 14:
                    A1 = inttoarr(_coef)
                    _ccc1 = _xors
                    flg1 = 1
                    cnt = cnt +1
                elif _coef == 19:
                    A2 = inttoarr(_coef)
                    _ccc2 = _xors
                    flg2 = 1
                    cnt = cnt +1
                elif _coef == 25:
                    A3 = inttoarr(_coef)
                    _ccc3 = _xors
                    flg3 = 1
                    cnt = cnt +1
                elif _coef == 28:
                    A4 = inttoarr(_coef)
                    _ccc4 = _xors
                    flg4 = 1
                    cnt = cnt +1
                elif _coef == 11:
                    A5 = inttoarr(_coef)
                    _ccc5 = _xors
                    flg5 = 1
                    cnt = cnt +1
                elif _coef == 26:
                    A6 = inttoarr(_coef)
                    _ccc6 = _xors
                    flg6 = 1
                    cnt = cnt +1
                if cnt == 6:
                    if groups.count(_groups)>0:
                        _index = groups.index(_groups)
                        print "removing" , _groups
                        groups.pop(_index)
                        coef.pop(_index)
                        xors.pop(_index)
                    if flg0 == 1 and flg1 == 1 and flg2 == 1 and flg3 ==1 and flg4 == 1:
                        solved = solved + 1
                        print "Group : ", _groups," Solved : ", solved
                        print flg0,flg1,flg2,flg3,flg4,flg5,flg6
                        ccc0 = _ccc0
                        ccc1 = _ccc1                    
                        ccc2 = _ccc2
                        ccc3 = _ccc3
                        ccc4 = _ccc4
                        A[0] = A0
                        A[1] = A1
                        A[2] = A2
                        A[3] = A3
                        A[4] = A4
                    elif flg0 == 0 and flg1 == 1 and flg2 == 1 and flg3 ==1 and flg4 == 1:
                        solved = solved + 1
                        print "Group : ", _groups," Solved : ", solved
                        print flg0,flg1,flg2,flg3,flg4,flg5,flg6
                        ccc0 = _ccc6
                        ccc1 = _ccc1                    
                        ccc2 = _ccc2
                        ccc3 = _ccc3
                        ccc4 = _ccc4
                        A[0] = A6
                        A[1] = A1
                        A[2] = A2
                        A[3] = A3
                        A[4] = A4
                    elif flg0 == 1 and flg1 == 0 and flg2 == 1 and flg3 ==1 and flg4 == 1:
                        solved = solved + 1
                        print "Group : ", _groups," Solved : ", solved
                        print flg0,flg1,flg2,flg3,flg4,flg5,flg6
                        ccc0 = _ccc0
                        ccc1 = _ccc6                    
                        ccc2 = _ccc2
                        ccc3 = _ccc3
                        ccc4 = _ccc4
                        A[0] = A0
                        A[1] = A6
                        A[2] = A2
                        A[3] = A3
                        A[4] = A4
                    elif flg0 == 1 and flg1 == 1 and flg2 == 0 and flg3 ==1 and flg4 == 1:
                        solved = solved + 1
                        print "Group : ", _groups," Solved : ", solved
                        print flg0,flg1,flg2,flg3,flg4,flg5,flg6
                        ccc0 = _ccc0
                        ccc1 = _ccc1                    
                        ccc2 = _ccc6
                        ccc3 = _ccc3
                        ccc4 = _ccc4
                        A[0] = A0
                        A[1] = A1
                        A[2] = A6
                        A[3] = A3
                        A[4] = A4
                    elif flg0 == 1 and flg1 == 1 and flg2 == 1 and flg3 ==0 and flg4 == 1:
                        solved = solved + 1
                        print "Group : ", _groups," Solved : ", solved
                        print flg0,flg1,flg2,flg3,flg4,flg5,flg6
                        ccc0 = _ccc0
                        ccc1 = _ccc1                    
                        ccc2 = _ccc2
                        ccc3 = _ccc5
                        ccc4 = _ccc4
                        A[0] = A0
                        A[1] = A1
                        A[2] = A2
                        A[3] = A5
                        A[4] = A4
                    elif flg0 == 1 and flg1 == 1 and flg2 == 1 and flg3 ==1 and flg4 == 0:
                        solved = solved + 1
                        print "Group : ", _groups," Solved : ", solved
                        print flg0,flg1,flg2,flg3,flg4,flg5,flg6
                        ccc0 = _ccc0
                        ccc1 = _ccc1                    
                        ccc2 = _ccc2
                        ccc3 = _ccc3
                        ccc4 = _ccc5
                        A[0] = A0
                        A[1] = A1
                        A[2] = A2
                        A[3] = A3
                        A[4] = A5
                    flg0 = 0
                    flg1 = 0
                    flg2 = 0
                    flg3 = 0
                    flg4 = 0
                    flg5 = 0
                    flg6 = 0
                        
                    
                    
                    #----------------------------------------------
                    # Creating And Solving The Set Of XOR Equations
                    #----------------------------------------------
                    cnt = 0
                    nw = 1
                    for ii in range(0,1024):
                        AA =  [[A[j][i] for i in range(0,5)] for j in range(0,5)]
                        s = [1,1,1,1,1]
                        s[0] = ord(charN(ccc0,ii))
                        s[1] = ord(charN(ccc1,ii))
                        s[2] = ord(charN(ccc2,ii))
                        s[3] = ord(charN(ccc3,ii))
                        s[4] = ord(charN(ccc4,ii)) 
                        x = SolveLinearSystem (AA, s, 5)  #Solving each partial equatoin
                        cal0.append(chr(x[0]))            #Collecting partial solutions
                        cal1.append(chr(x[1]))
                        cal2.append(chr(x[2]))
                        cal3.append(chr(x[3]))
                        cal4.append(chr(x[4]))
                    #print len(cal0)
                    p0 = _join(cal0)                      #Joining 1024 bytes together 
                    p1 = _join(cal1)
                    p2 = _join(cal2)
                    p3 = _join(cal3)
                    p4 = _join(cal4)
                    #print len(cal0)
                    
                    #----------------------------------------------
                    # ----------                       ------------
                    #----------------------------------------------
                    
                    playlist.append(p0)
                    playlist.append(p1)
                    playlist.append(p2)
                    playlist.append(p3)
                    playlist.append(p4)
                    
            # ------------------------------------------------------------                    
            # Removing incomplete groups - Groups With Less Than 5 Members
            # ------------------------------------------------------------
            if _groups != cur:
                cnt = 1
                nw = 0
                #print "---------------------------------", cur, "  " , _groups
                while len(_ccc)>0 :
                    _ccc.pop(0)
                cur = _groups
                A[cnt] = inttoarr(_coef)
                _ccc.append(_xors)
                
                
#------------------------------------------------------------------------
#------------------------------------------------------------------------
                
def play(stream, CHUNK):
    while True:
            if len(playlist) > 1:
                #print "--------------------------------", len(playlist)
                a = playlist.pop(0)
                stream.write(a)                   
                
#------------------------------------------------------------------------
#------------------------------------------------------------------------
          
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
    return B

#------------------------------------------------------------------------
#------------------------------------------------------------------------

def arrtoint(s):
	x=0
	x=x+s[0]
	x=(x*2)+s[1]
	x=(x*2)+s[2]
	x=(x*2)+s[3]
	x=(x*2)+s[4]
	return x

ss = [4,6,8,9,1]
                
#------------------------------------------------------------------------
#------------------------------------------------------------------------
          
def inttoarr(i):
	a = [0,0,0,0,0]
	le = len(a)
	x4 = i%2
	a[4] = x4
	i = i/2
	x3 = i%2
	a[3] = x3
	i = i/2
	x2 = i%2
	a[2] = x2
	i = i/2
	x1 = i%2
	a[1] = x1
	i = i/2
	x0 = i%2
	a[0] = x0
	return a

#------------------------------------------------------------------------
#------------------------------------------------------------------------
          
def _join(str):
    length = len(str)
    return ''.join(str.pop(0)     for i in xrange(length))
def charN(str, N):
    if N < len(str):
        return str[N]
    return 'X'
                
#------------------------------------------------------------------------
#------------------------------------------------------------------------
          
if __name__ == "__main__":
    FORMAT = pyaudio.paInt16
    CHUNK = 8192
    CHANNELS = 1
    RATE = 10240
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    output = True,)
                    #frames_per_buffer = CHUNK,
                    #)
    #pkt2 = packet(stream.read(CHUNK))
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind((UDP_A, 5000))

    Ts = Thread(target = udpStream, args=(udp, CHUNK,))
    Tp = Thread(target = play, args=(stream, CHUNK,))
    Tr = Thread(target = extract)
    Ts.setDaemon(True)
    Tp.setDaemon(True)
    Tr.setDaemon(True)
    Ts.start()
    Tp.start()
    Tr.start()
    Ts.join()
    Tp.join()
    Tr.join()

    udp.close()
                
#------------------------------------------------------------------------
#------------------------------------------------------------------------                
#------------------------------------------------------------------------
#------------------------------------------------------------------------
          
