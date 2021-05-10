import socket

domain = input('please input the domain name:')

hostip = socket.gethostbyname_ex(domain)

print("The IP address of the domain "+domain+" are below")

for iter in hostip[2]:
    print(iter)
    
    