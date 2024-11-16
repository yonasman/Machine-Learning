import socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect(('yonasnegese.netlify.app.com',80))
cmd = 'GET http://yonasnegese.netlify.app.com HTTP/1.1\n\n'.encode()
mySocket.send(cmd)

# while True:
#     data = mySocket.recv(500)
#     if(len(data) < 1):
#         break
#     print(data.decode())
# mySocket.close()


# **********
newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
newSocket.connect(('data.pr4e.org', 80))

# Correctly formatted HTTP GET request with the Host header
cmd2 = 'GET /intro-short.txt HTTP/1.1\r\nHost: data.pr4e.org\r\n\r\n'.encode()
newSocket.send(cmd2)

while True:
    data = newSocket.recv(500)
    if len(data) < 1:
        break
    # print(data.decode())

newSocket.close()
