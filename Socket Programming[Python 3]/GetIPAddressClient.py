import socket

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
clientSocket.bind(('127.0.0.1',0)) # defining port 0 means allowing to connect with any port

#lets take the domain from the user
domainName = input("Enter the domain : ")

clientSocket.sendto(domainName.encode(),('127.0.0.1',1225))
# domainName.encode() is used to encode the data in bytes
# as the server is expecting data in bytes
data,address = clientSocket.recvfrom(1024)

print("IP Address for ", domainName , "is : ",data.decode())
#decoding the data which is received in bytes

clientSocket.close()
