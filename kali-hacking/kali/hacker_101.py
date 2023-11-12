import socket

if __name__ == "__main__":
    hacker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    hacker_IP = "192.168.64.111" # kali linux IP
    hacker_port = 8008

    socket_address = (hacker_IP, hacker_port)
    hacker_socket.bind(socket_address)
    hacker_socket.listen(5)
    print("Listening for incoming connection requests ...")

    hacker_socket, client_address = hacker_socket.accept()
    message = "This is a message from hacker."
    message_bytes = message.encode()
    hacker_socket.send(message_bytes)
    print("Message from hacker sent")
    hacker_socket.close()