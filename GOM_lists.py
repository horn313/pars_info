GOM_new = []
GOM_old = []
def GOM_lists():
    with open('GOM.txt', 'r') as file:
        info = file.readlines()
    for i in info:
        i = i.replace('\n', '')
        GOM_new.append(i)


    with open('GOM_old.txt', 'r') as file:
        info = file.readlines()
    for i in info:
        i = i.replace('\n', '')
        GOM_old.append(i)

    return GOM_new, GOM_old

