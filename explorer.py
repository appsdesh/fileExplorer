import socket
import os

TCP_IP = '127.0.0.1'
TCP_PORT = 9999
ADDRESS = TCP_IP + ":" + str(TCP_PORT)
QUERY = 'http://' + ADDRESS + '?'
BUFFER_SIZE = 2000
MESSAGE = 'Hello World!'
HTML_HEADER_PROTO = """HTTP/1.0 200 OK"""
CONTENT_TYPE = """
Content-Type: """

HTML_BODY_HEAD = """<html><head><title>Success</title></head><body>"""
HTML_BODY_TRAIL = """</body></html>"""
DEFAULT_TYPE = """text/html""" + '\n\n'

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

def walkTheTree(currDir):
    body = '\n'
    for sub in os.listdir(currDir):
		body = body + '<a href=' + QUERY + os.path.join(currDir, sub) +'? >'+ sub + '</a><br />'
    body = body + '<a href=' + QUERY + os.path.dirname(currDir) +'? > .. </a><br />'
    return body
	
if __name__=='__main__':
   s = createTCPServer()
   try:
    s.listen(5)
    while True: 
			clientsock, addr = s.accept()
			data = clientsock.recv(BUFFER_SIZE)
			arr = data.split('?')
			print arr
			currDir = os.getcwd() if len(arr) < 3 else arr[1]
			print "Curr dir: " + currDir + "\n"
			body = walkTheTree(currDir)
			print "BODY ==>"+ body +"\n"
			clientsock.sendall(HTML_HEADER_PROTO + CONTENT_TYPE + DEFAULT_TYPE + HTML_BODY_HEAD + body + HTML_BODY_TRAIL) 
			clientsock.close()
   except Exception, err:
		print 'Error occured :' + str(err)

   
