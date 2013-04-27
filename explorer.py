import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 9999
ADDRESS = TCP_IP + ":" + str(TCP_PORT)

BUFFER_SIZE = 2000
MESSAGE = 'Hello World!'

def createTCPServer():
    try:
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     s.bind((TCP_IP, TCP_PORT))
    except socket.error, msg:
     print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    return s

def listenAndAccept(s):
    s.listen(5)
    conn, addr = s.accept()
    print 'Connection address:', addr
    return conn, addr
	
if __name__=='__main__':
   s = createTCPServer()
   clientsock, addr = listenAndAccept(s)
   clientsock.recv(BUFFER_SIZE)
   clientsock.sendall(MESSAGE)
   clientsock.close()
   s.close()
   
