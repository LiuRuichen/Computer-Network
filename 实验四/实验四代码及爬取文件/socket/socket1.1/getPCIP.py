import socket

hostname = socket.gethostname()  # 本地主机名
hostip = socket.gethostbyname_ex(hostname)  # 原始主机名，域名列表，IP地址列表
print("This computer is "+str(hostname))

print("Its IP addresses are:")

for iter in hostip[2]:
    print(iter)

    
    
    
    
    