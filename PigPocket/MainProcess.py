from Users import Users

#you are required to do exception handling

def processUser():
    usersList = []
    user_file = open('file/users.txt', 'r')
    for ulist in user_file:
        list = ulist.split(',')
        s = Users(list[0], list[1], int(list[2]))

        usersList.append(s)
    return usersList

def processTransaction(firstname, month, type):
    t_file = open('file/transaction.txt', 'r')
    total = 0
    for trans in t_file:
        list = trans.split(',')

        if list[0] == firstname and list[1] == month and list[2] == type:
            total += float(list[3])
    return total

def registerNewUser(name, id, password):
    userdata = name + ',' + id + ',' + password + '\n'
    user_file = open('file/users.txt', 'a')
    user_file.write(userdata)

