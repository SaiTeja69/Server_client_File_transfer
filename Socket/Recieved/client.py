import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.

s.connect((host, port))
#s.send("Hello server!")

f=open('received_file.txt', 'wb') 
print('receiving data...')
data = s.recv(1024)
f.write(data)

f.close()
print('File Transfer Successfull')
s.close()
print('connection closed')
