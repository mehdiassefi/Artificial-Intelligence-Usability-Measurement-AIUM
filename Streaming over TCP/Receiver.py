import pyaudio
import socket
import sys
 
chunk = 1024
p = pyaudio.PyAudio()
 
stream = p.open(format = pyaudio.paInt16,
                channels = 1,
                rate = 10240,
                output = True)
 

TCP_IP = ''
TCP_PORT = 50000
BUFFER_SIZE = 1024
backlog = 5  
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(backlog)
backlog = 5
client, address = s.accept()
sum = 0
while 1:
    data = client.recv(size)
    if data:
	sum += len(data)
        #print sum
	stream.write(data)
        #client.send('ACK')
client.close()
stream.close()
