import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    #Create a communication port for the UDP protocolo using DATAGRAM
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #Associating the address and the port to a process
    s.bind((host, port))

    print("Server started.")

    while True:
        #Establishing the max queue size for the accepted connection
        # and receive messagge from client
        data, address = s.recvfrom(1024)

        print("Messagge from: " + str(address))
        print("From connect user : " + str(data))
        data = str(data).upper()
        print("Sending : " + str(data))
        #Sending the message to the client
        s.sendto(data.encode(), address)
    s.close()

if __name__ == '__main__':
    Main()
