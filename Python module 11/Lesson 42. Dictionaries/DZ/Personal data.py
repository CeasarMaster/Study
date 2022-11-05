information = input().split()

info = {}
info['Name'] = information[0]
info['Surname'] = information[1]
info['City'] = information[2]
info['School'] = information[3]
info['Marks'] = information[4:]
for i in info:
    print(i, '-', info[i])
