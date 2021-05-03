import socket
import select
import msvcrt
import conf


def print_client_sockets(client_sockets):
    for c in client_sockets:
        print(c.getpeername())


print("Setting up server...")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((conf.SERVER_IP, conf.SERVER_PORT))
server_socket.listen()
print("Listening for clients...")

client_sockets = []
messages_to_send = []


while True:
    rlist, wlist, xlist = select.select([server_socket] + client_sockets, client_sockets, [])
    for current_socket in rlist:
        if current_socket is server_socket:
            connection, client_address = current_socket.accept()
            print("New client joined!", client_address)
            client_sockets.append(connection)

        else:
            data = current_socket.recv(conf.MAX_MSG_LENGTH).decode()

            if data == "":
                print("Connection closed", )
                client_sockets.remove(current_socket)
                current_socket.close()
            else:
                messages_to_send.append((current_socket, data))


    for message in messages_to_send:
        current_socket, data = message
        if current_socket in wlist:
            for i in range(0, len(client_sockets)):
                if(client_sockets[i] != current_socket):
                    client_sockets[i].send(("client sent: " + data + "\r").encode())

            messages_to_send.remove(message)
