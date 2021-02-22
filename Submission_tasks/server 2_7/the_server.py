import socket
import protocol
import conf27


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((conf27.PROTOCOL_IP, conf27.PROTOCOL_PORT))
server_socket.listen()
print("Server is up and running")
(client_socket, client_address) = server_socket.accept()

while(conf27.tnai_server_to_run == True):
    try:
        client_commend_length = client_socket.recv(5).decode("utf-8")
        client_commend = client_socket.recv(int(client_commend_length)).decode("utf-8")
    except Exception as e:
        print("cannot receive massage from client")
        print("the problem is: " + e)

    try:
        if(protocol.CHECK_IF_COMMAND_TO_SERVER_IS_CURECT(client_commend) == True):
            client_socket.send(str("00004True").encode("utf-8"))
            tnai_is_commend_good = True
        elif(protocol.CHECK_IF_COMMAND_TO_SERVER_IS_CURECT(client_commend) == False):
            client_socket.send(str("00005False").encode("utf-8"))
            tnai_is_commend_good = False

    except Exception as e:
        print("cannot send massage to client")
        print("the problem is: " + e)


    #for the DIR commend
    if(client_commend == "DIR") and (tnai_is_commend_good == True):
        try:
            files_list = protocol.DIR()

            print("the files are:")
            for i in range(0, len(files_list)):
                print(files_list[i])
            print("")

        except Exception as e:
            print("cannot dir files")
            print("the problem is: " + e)


    #for the DELETE commend
    if(client_commend == "DELETE") and (tnai_is_commend_good == True):
        try:
            print("the files names are:")
            print(protocol.FILES_IN_FOLDER())
            file_name = input()

            if(protocol.WROTE_WRONG_FILE(file_name) == False):
                while(protocol.WROTE_WRONG_FILE(file_name) == False):
                    print("you wrote a bad file name")
                    print("the files names are:")
                    print(protocol.FILES_IN_FOLDER())
                    file_name = input()

            if (protocol.WROTE_WRONG_FILE(file_name) == True):
                file_name = file_name + ".txt"
                protocol.DELETE(file_name)
                client_socket.send("00008continue".encode("utf-8"))

        except Exception as e:
            print("cannot delete file")
            print("the problem is: " + e)


    #for the COPY commend
    if(client_commend == "COPY") and (tnai_is_commend_good == True):
        try:
            print("the files names are:")
            print(protocol.FILES_IN_FOLDER())
            file_name = input()

            if(protocol.WROTE_WRONG_FILE(file_name) == False):
                while(protocol.WROTE_WRONG_FILE(file_name) == False):
                    print("you wrote a bad file name")
                    print("the files names are:")
                    print(protocol.FILES_IN_FOLDER())
                    file_name = input()

            if (protocol.WROTE_WRONG_FILE(file_name) == True):
                file_name = file_name + ".txt"
                protocol.COPY(file_name)
                client_socket.send("00008continue".encode("utf-8"))

        except Exception as e:
            print("cannot copy file")
            print("the problem is: " + e)


    #for EXECUTE commend
    if(client_commend == "EXECUTE") and (tnai_is_commend_good == True):
        try:
            protocol.EXECUTE()

        except Exception as e:
            print("cannot execute")
            print("the problem is: " + e)


    #for TAKE_SCREENSHOT commend
    if(client_commend == "TAKE_SCREENSHOT") and (tnai_is_commend_good == True):
        try:
            protocol.TAKE_SCREENSHOT()

        except Exception as e:
            print("cannot take screenshot")
            print("the problem is: " + e)


    #for SEND_PHOTO commend
    if(client_commend == "SEND_PHOTO") and (tnai_is_commend_good == True):
        try:
            my_pic = protocol.SEND_PHOTO()
            length = str(len(my_pic))
            zfill_length = length.zfill(10)


            client_socket.send(str(zfill_length).encode("utf-8"))
            client_socket.send(my_pic)

        except Exception as e:
            print("cannot send photo")
            print("the problem is: " + e)


    if(client_commend == "EXIT") and (tnai_is_commend_good == True):
        client_socket.close()
        server_socket.close()
        exit(1)
