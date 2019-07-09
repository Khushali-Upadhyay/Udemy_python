Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #ZDownload images and access url using urllib
>>> #Socket programming connection between client and server using socket
>>> #Sending email by suing smtplib
>>> #Downloading html
>>> import urllib.request
>>> try:
	url=urllib.request.urlopen()"http://www.python.org)
	
SyntaxError: EOL while scanning string literal
>>> try:
	url=urllib.request.urlopen("http://www.python.org/")
	content=url.read()
	url.close()
except urllib.error.HTTPError:
	print("The web page is not found")
	exit()

	
>>> f=open('python.html','wb')
>>> f.write(content)
48169
>>> f.close()
>>> 
>>> #Downloading image
>>> import urllib.request
>>> urllib.request.urlretrieve("http://www.python.org/static/img/python-logo@2x.png","python.png")
('python.png', <http.client.HTTPMessage object at 0x000000CF3A478BE0>)
>>> 
>>> #Create a server
>>> import socket
>>> host='localhost'
>>> port=4000
>>> s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
>>> s.bind((host,port))
>>> print("Server listening on port:",port)
Server listening on port: 4000
>>> s.listen(1)
>>> c,addr=s.accept()
print("Connection from:",str(addr))
c.send(b"Hello, How are you")
c.send("bye".encode())
c.close()
#Create a client
import socket
s=socket.socket()
s.connect(("localhost",4000))
msg=s.recv(1024)
while msg:
	print("Received: ",msg.decode())
	msg=s.recv(1024)

s.close()
#File Client
import socket
host='localhost'
port=6767
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
print("Server listening on port:",port)
s.listen(1)
c,addr=s.accept()
fileName=c.recv(1024)
try:
	f=open(fileName,'rb')
	content=f.read()
	c.send(content)
	f.close()
except FileNotFoundError:
	c.send(b"File Doesnt exist")
c.close()
#File Client
import socket
s=socket.socket()
s.connect(("localhost",4000))
fileName=input("Enter a file name:")
s.send(fileName.encode())
content=s.recv(1024)
print(content.decode())
s.close()

