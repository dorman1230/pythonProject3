import socket
import conf27
import protocol


my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect((conf27.CLIENT_IP, conf27.SERVER_PORT))


while(conf27.tnai_client_to_run == True):
    protocol.commend_list()
    command = input()
    command_length = str(len(command))
    zfill_length = command_length.zfill(5)
    commend_to_server = zfill_length + command

    try:
        my_socket.send(commend_to_server.encode("utf-8"))

        length_is_good_commend = my_socket.recv(5).decode("utf-8")
        is_good_commend = my_socket.recv(int(length_is_good_commend)).decode("utf-8")
    except Exception as e:
        print("cannot continue")
        print("the problem is: " + e)


    if(is_good_commend == "False"):
        print("you wrote a bad commend")


    if(command == "DELETE") and (is_good_commend == "True"):
        try:
            when_to_continue = my_socket.recv(5).decode("utf-8")
            to_continue = my_socket.recv(int(when_to_continue)).decode("utf-8")
        except Exception as e:
            print("cannot receive massage to continue from server")
            print("the problem is: " + e)


    if(command == "COPY") and (is_good_commend == "True"):
        try:
            when_to_continue = my_socket.recv(5).decode("utf-8")
            to_continue = my_socket.recv(int(when_to_continue)).decode("utf-8")
        except Exception as e:
            print("cannot receive massage to continue from server")
            print("the problem is: " + e)


    if(command == "SEND_PHOTO") and (is_good_commend == "True"):
        try:
            size = int(my_socket.recv(10).decode())
            data = my_socket.recv(size)
            my_file = open(conf27.path_for_photo_client_side, "wb")
            my_file.write(data)
            my_file.close()
        except Exception as e:
            print("cannot receive photo from server")
            print("the problem is: " + e)


    if(command == "EXIT") and (is_good_commend == "True"):
        my_socket.close()
        exit(1)
