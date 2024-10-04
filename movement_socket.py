import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8083))
server_socket.listen(1)

client_socket, client_address = server_socket.accept()

while True:
    command = client_socket.recv(1024).decode()

    movement, rotation = command.split(",")

    if movement == "forward":
        pass
    elif movement == "backward":
        pass
    elif movement == "stop":
        pass

    if rotation == "left":
        pass
    elif rotation == "right":
        pass
    elif rotation == "stop":
        pass

    if movement == "exit" and rotation == "exit":
        break

    print(f"Received: {command} from client")

client_socket.close()
server_socket.close()
