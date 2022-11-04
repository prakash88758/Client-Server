import socket


def client():
    host = socket.gethostname()
    # get the hostname

    port = 5000
    # get the port number

    client = socket.socket()
    # get instance of socket

    client.connect((host, port))
    # connect to the server
    
    prompt = """
BD = binary to decimal 
DB = decimal to binary 
HD = hexadecimal to binary 
DH = decimal to binary 
Enter conversion type:"""
    source = {
        'd': 'Decimal',
        'b': 'Binary',
        'h': 'Hexadecimal'
    }
    
    print("Enter operations to get result and 'end' to exit: ")
    print(prompt)
    method = input("Method: ").lower()
    number = input(source[method[0]] + " Number: ")
    message = method + " " + number
    # get the input from the user

    while message.lower().strip() != 'end':
        # while the message is not 'end', keep sending the message

        client.send(message.encode())
        # encode the message and send it to the server

        data = client.recv(1024).decode()
        # receive data from the server

        print('Result received from server: ' + data)
        # print the data received from the server
    
        method = input("Method: ").lower()
        number = input(source[method[0]] + " Number: ")
        message = method + " " + number
        # get the next message from the user

    client.close()
    # close the connection


if __name__ == '__main__':
    client()
