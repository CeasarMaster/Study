def ip_address(num, count, string):
    if count == len(num):
        ip.append(string)
        print(ip)
        return 0
    else:
        if num[count].isdigit():
            string += num[count]
        else:
            ip.append(string)
            string = ''
        return ip_address(num, count + 1, string)


n = input('Insert the number: ')
x = ''
ip = []
counter = 0
ip_address(n, counter, x)
'''while counter < len(n):
    if n[counter].isdigit():
        x += n[counter]

    else:
        ip.append(x)
        x = ''
    counter += 1
ip.append(x)
print(ip)'''
