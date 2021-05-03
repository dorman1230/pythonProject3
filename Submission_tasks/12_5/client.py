
import socket
import sys
import select
import msvcrt

# Constants
SERVER = '127.0.0.1'  # TODO: Change this
PORT = 50000

TIMEOUT = 0.1  # Timeout, in seconds, for select command
SOCKET_BUFFER_SIZE = 1024


def send_chat_message(active_socket, message):
    """
    Gets a socket and sends the requested message.
    """
    active_socket.send(message.encode())


def receive_from_server(active_socket):
    """
    Receives data from server. Loops until the received buffer is smaller than
    the buffer maximal size. Returns the data.
    """
    buffer_data = active_socket.recv(SOCKET_BUFFER_SIZE).decode("utf-8")
    final_data = buffer_data

    # Attempt to receive the whole message!
    while len(buffer_data) >= SOCKET_BUFFER_SIZE:
        buffer_data = active_socket.recv(SOCKET_BUFFER_SIZE).decode("utf-8")
        final_data += buffer_data

    return final_data


# Create the main socket - connection with the server
try:
    # Create a TCP socket
    # AF_INET means IPv4.
    # SOCK_STREAM means a TCP connection.
    # SOCK_DGRAM would mean an UDP "connection".
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server
    sock.connect((SERVER, PORT))
    print('Connected to the server!')

except socket.error as e:
    # An error occurred
    print('Error connecting to server!')
    # Quit
    sys.exit(1)

# Run this loop forever...
input_from_user = ''
while True:
    try:
        # Wait for input from the server socket
        rlist, wlist, xlist = select.select([sock], [sock], [])

        for current_socket in rlist:
            # We have a message from the server!
            data = receive_from_server(sock)
            if data == "":
                # We failed to receive data. The connection terminated.
                print('Shutting down.')
                sys.exit(1)
            else:
                # We received the data successfully! Write it to the user!
                print(data)

        # Try to read from the user
        # Note that this code is non blocking so a read operation on the socket
        # is also possible if any key was pressed
        if msvcrt.kbhit():
            # Save the key that was pressed
            keypressed = msvcrt.getche()
            # Present the key on the screen for the user to see
            sys.stdout.write(str(keypressed.decode()))
            # if the key that was pressed was <Enter>:
            if keypressed.decode() == '\r' or keypressed.decode() == '\n':
                sys.stdout.write('\n')
                # input_from_user is ready, so we can use it!
                # We want to send the message to the server...
                send_chat_message(sock, input_from_user + "\n")
                # Initialize input_from_user
                input_from_user = ''

            else:
                # input_from_user is not ready, so concatenate the pressed key
                input_from_user += str(keypressed.decode())

    except KeyboardInterrupt:
        print ('Interrupted.')
        sock.close()
        break
