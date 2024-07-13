#iFridge
#API course
#(c) Daniel Smigala, Yasmine Hildebrand, Constantin Denden, Julius Schieck, David Nagel

import ui_Usermanagement

UserManagement = ui_Usermanagement.UserManagementInstanz


def UsersToString():
    usersstring = ""
    users = UserManagement.get_all_users()
    index = 0
    while (index < len(users)):
        usersstring += str( str(users[index]["name"]) + ";" + str(users[index]["balance"]) + ";" + "/n" )
        index += 1
    return usersstring

def ExportUsers(path = "Users.txt"):
    file = open(path, "w")
    file.write(UsersToString())
    file.close()


def ImportUsers(path = "Users.txt"):
    file = open(path, "r")
    for line in file:
        userstring = file.readline()
        username = ""
        userbalance = ""
        index = 0
        row = 0
        while index < len(userstring):
            if (userstring[index] != ";"):
                if (row == 0):
                    username += str(userstring[index])
                if (row == 1):
                    userbalance += str(userstring[index])
            else:
                row += 1
            index += 1
        if (username != "") and (userbalance != ""):
            userbalance = int(userbalance)
            UserManagement.add_user(username, userbalance)


