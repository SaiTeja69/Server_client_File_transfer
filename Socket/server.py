import socket                   # Import socket module

port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind(('', port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print ('Server listening....')
conn, addr = s.accept()     # Establish connection with client.
print ('Got connection from', addr)
filename='order.txt'
f = open(filename,'rb')
l = f.read(1024)
conn.send(l)
print('Done sending')
print('Thank you for connecting')
conn.close()
