import socket
import datetime
import random

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 7777))
server_socket.listen()
print("server is running:")

tnai_to_stop_big_while_loop = False
tnai_to_stop_massage_while_loop = False
tnai_to_start_recv_in_massage_while_loop = 0

while(tnai_to_stop_big_while_loop == False):
    (client_socket, client_address) = server_socket.accept()

    user_commendID = client_socket.recv(1).decode("utf-8")
    user_massage_length = client_socket.recv(2).decode("utf-8")
    user_massage = client_socket.recv(int(user_massage_length)).decode("utf-8")
    print("user sent: " + user_massage)


    if(user_commendID == "0"):

        tnai_to_stop_massage_while_loop = False
        tnai_to_start_recv_in_massage_while_loop = 0
        user_massage = "null"

        while(tnai_to_stop_massage_while_loop == False):
            if(tnai_to_start_recv_in_massage_while_loop >= 1) or (user_massage == "stop texting"):
                user_commendID = client_socket.recv(1).decode("utf-8")
                user_massage_length = client_socket.recv(2).decode("utf-8")
                user_massage = client_socket.recv(int(user_massage_length)).decode("utf-8")
                print("user sent: " + user_massage)

            if(user_massage == "stop texting"):
                tnai_to_stop_massage_while_loop = True
                client_socket.send(str("08good baye").encode("utf-8"))

            if(user_massage != "stop texting"):
                print("Enter your massage:")
                massage = input()
                length_massage = str(len(massage))
                zfill_length = length_massage.zfill(2)
                return_from_server = zfill_length + massage

            client_socket.send(str(return_from_server).encode("utf-8"))

            tnai_to_start_recv_in_massage_while_loop = tnai_to_start_recv_in_massage_while_loop + 1


    if(user_commendID == "1"):
        date = datetime.datetime.now()
        str_date = str(date)
        length = str(len(str_date))
        zfill_length = length.zfill(2)

        return_from_server = zfill_length + str_date


    if(user_commendID == "2"):
        name = "The Master"
        length = str(len(name))
        zfill_length = length.zfill(2)
        return_from_server = zfill_length + name


    if (user_commendID == "3"):
        num = random.randint(1, 10)
        number = str(num)
        length = str(len(number))
        zfill_length = length.zfill(2)
        return_from_server = zfill_length + str(number)


    if (user_commendID == "4"):
        tnai_to_stop_big_while_loop = True
        return_from_server = "03END"

    if (user_massage != "stop texting"):
        client_socket.send(str(return_from_server).encode("utf-8"))

client_socket.close()
server_socket.close()
