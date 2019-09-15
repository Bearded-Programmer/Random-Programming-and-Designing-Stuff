import socket

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#Here AF_INET represents the address family IPv4 which uses IP + Port for connection
#Lets bind the created serverSocket to an address
serverSocket.bind(('127.0.0.1',1225))

if serverSocket is not None:
    print("Server is up & running ... ")
    while 1:
        data,address = serverSocket.recvfrom(1024) # here 1024 represents the buffer size
        print("Connection request from : ",address)
        serverSocket.sendto(socket.gethostbyname(data),address)
else:
    print("Server creation failed")

#you can refer official  Python docs to know more about socket module.
