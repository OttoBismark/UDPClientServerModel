import socket

def Main():
    host = '127.0.0.1'
    port = 5001 #Different port this time, because we don't know the specific
                #server port to establish a connection

    #Create a tuple {Server_address, Server_port}
    server = (host, 5000)
    #Creating a socket for the communication
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #Binding address and port to a process
    s.bind((host, port))

    #Function to type a message to send to the server
    message = input("-> ")

    while message != 'q':
        #Send a message to the server
        s.sendto(message.encode(), server)
        #Receive the message from the server
        data, address = s.recvfrom(1024)
        print("Received from server " + str(data))
        message = input("-> ")

    s.close()


if __name__ == '__main__':
    Main()
