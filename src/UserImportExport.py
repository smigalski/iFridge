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
        usersstring.append(str(users[index]["name"]) + ";" + str(users[index]["balance"]) + ";" + "/n")
        index += 1
    return usersstring

def ExportUsers(path = "Users.txt"):
    file = open(path, "w")
    file.write(UsersToString())
    file.close()





