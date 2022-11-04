import socket

def server():
    # get the hostname
    host = socket.gethostname()
    port = 5000

    server = socket.socket()
    # get instance of socket

    server.bind((host, port))
    # bind the socket to the host and port

    server.listen(10)
    # listen for 10 connections

    conn, addr = server.accept()
    # accept the connection

    while True:
        data = conn.recv(1024).decode()
        # receive data from the client

        if data == 'end':
            break

        operation, num1 = data.split(' ')
        # split the data into two numbers

        print("Received request from client: ", data)
        # print the data received from the client

        if operation == 'bd':
            result = int(num1, 2)
        elif operation == 'db':
            result = str(bin(int(num1))).upper()
        elif operation == 'hd':
            result = int(num1, 16)
        elif operation == 'dh':
            result = str(hex(int(num1))).upper()
        else:
            result = 'Invalid operation'
        # Perform the operation

        print('Sending result to client: ', result)

        conn.send(str(result).encode())
        # send the result back to the client

    conn.close()
    # close the connection


if __name__ == '__main__':
    server()
