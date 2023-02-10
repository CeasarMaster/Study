import socket

hostname = input('Insert the website link:\n')

print(f'Hostname: {hostname}\nIP of {hostname}: {socket.gethostbyname(hostname)}')
