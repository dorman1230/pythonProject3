import glob
import os
import conf27
import shutil
import subprocess
import pyautogui


def DIR():
    """
    this protocol show the server the path of all the files in the tikia

    :param: files
    :type files: String

    :return: files
    :return type: String
    """
    if (os.path.isdir(conf27.the_files_path)):
        files = glob.glob(conf27.the_files_path + '\*.*')

    return files


def DELETE(what_to_delete):
    """
    the client choose one file to delete then this protocol check if the file exists and if
    the file exists the protocol takes the file and delete him and if the file does not
    exists the protocol does not do enithing

    :param: what_to_delete
    :param: path_to_delete

    :type what_to_delete: String
    :type path_to_delete: String

    :return: null
    :return type: null
    """
    path_to_delete = r"C:\Users\עמית\PycharmProjects\pythonProject3\Submission_tasks\server 2_7\file_for_submission_task\"" + \
                     str(what_to_delete)
    path_to_delete = path_to_delete.replace('"', '')

    os.remove(path_to_delete)


def COPY(what_to_copy):
    """
    the client choose one file and then this protocol check if the file exists and if
    the file exists the protocol takes the tochen of the file and copy him into another
    file and if the file does not exists the protocol does not do enifing

    :param: what_to_copy
    :param: copy_path
    :param: conf27.path_to_copy

    :type what_to_copy: String
    :type copy_path: String
    :type conf27.path_to_copy: String

    :return: null
    :return type: null
    """
    copy_path = r"C:\Users\עמית\PycharmProjects\pythonProject3\Submission_tasks\server 2_7\file_for_submission_task\"" + \
                str(what_to_copy)
    copy_path = copy_path.replace('"', '')

    shutil.copy(copy_path, conf27.path_to_copy)


def EXECUTE():
    """
    this protocol open notes

    :param: null
    :param type: null

    :return: null
    :return type: null
    """
    subprocess.call(r'C:\Windows\system32\notepad.exe')


def TAKE_SCREENSHOT():
    """
    this protocol gets fro, the server the photo name that the client chose
    and after that he save the photo in folder

    :param: null
    :param type: null

    :return: null
    :return type: null
    """

    image = pyautogui.screenshot()
    image.save(conf27.path_for_photo_server_side)


def SEND_PHOTO():
    """
    this protocol send the photo to the client

    :param:

    :return: null
    :return type: null
    """

    my_file = open(conf27.path_for_photo_server_side, "rb")
    my_pic = my_file.read()

    return my_pic



def CHECK_IF_COMMAND_TO_SERVER_IS_CURECT(command_to_server):
    """
    this protocol check that the command that the client send to the
    server exist in the command list

    :param: command_to_server
    :param: return_to_client

    :type command_to_server: String
    type return_to_client: boolean

    :return: return_to_client
    :return type: boolean
    """
    return_to_server_if_commend_is_correct = False

    if (command_to_server == "TAKE_SCREENSHOT"):
        return_to_server_if_commend_is_correct = True
    if (command_to_server == "SEND_PHOTO"):
        return_to_server_if_commend_is_correct = True
    if (command_to_server == "DIR"):
        return_to_server_if_commend_is_correct = True
    if (command_to_server == "DELETE"):
        return_to_server_if_commend_is_correct = True
    if (command_to_server == "COPY"):
        return_to_server_if_commend_is_correct = True
    if (command_to_server == "EXECUTE"):
        return_to_server_if_commend_is_correct = True
    if (command_to_server == "EXIT"):
        return_to_server_if_commend_is_correct = True

    return return_to_server_if_commend_is_correct


def FILES_IN_FOLDER():
    """
    this protocol take the adrasas of the files and delete every thing
    exept the name of the file (this protocol ment to be used by other
    protocols)

    :parm: files
    :parm: files_length

    :type files: String
    :type files_length: int

    :return: files
    :return type: String
    """

    files = DIR()
    files_length = len(files)

    for i in range(0, files_length):
        place_file_name = files[i]
        # this remove the all of the adrees and the ".txt" and leaves us just the name of the file
        files[i] = place_file_name[98:len(place_file_name) - 4]

    return files


def WROTE_WRONG_FILE(file_name):
    """
    if the client wrote to the server a file that does not exist the protocol tells him
    to write another file

    :param: name_list
    :param: name_is_good

    :type name_list: String
    :type name_is_good: boolean

    :return: name_is_good
    :return type: boolean
    """
    name_is_good = False

    name_list = FILES_IN_FOLDER()

    for i in range(0, len(name_list)):
        if (file_name == name_list[i]):
            name_is_good = True

    return name_is_good


def commend_list():
    print('Available commands are:')
    print('* TAKE_SCREENSHOT= This command takes a screenshot of the computer and saves it on the servers side')
    print('* SEND_PHOTO= This command takes the screenshot from the servers side and sends it to the client')
    print('* DIR= This command shows the server the path to all the text files')
    print('* DELETE= This command deletes any text file that the server selects')
    print('* COPY= This command copies the text of any text file that the server selects to another text file')
    print('* EXECUTE= This command opens a new text file document')
    print('* EXIT= This command terminates the server and client activity')
