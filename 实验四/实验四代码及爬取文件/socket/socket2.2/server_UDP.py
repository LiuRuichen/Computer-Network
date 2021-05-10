#server
import socket
#创建Socket时， SOCK_DGRAM 指定了这个Socket的类型是UDP。

i = 0
addr = {}
server = socket.socket(type=socket.SOCK_DGRAM)
host = socket.gethostname()
server.bind((host,9999))
for i in range(0,4):    
    data,address = server.recvfrom(1024)
    addr[str(i+1)] = address[1]
    
print(addr)

strl = ""
for key,val in addr.items():
    strl = strl + "client " + key + "^" + str(val) + "&"
for val in addr.values():
    server.sendto(strl.encode('utf-8'),(host,val))

server.sendto("".encode('utf-8'),(host,addr['3']))
server.sendto("".encode('utf-8'),(host,addr['4']))

        
while True:
    
    data,address = server.recvfrom(1024)
    
    data = data.decode('utf-8')
      
    data_divided = data.split('/')
    
    print("We server receive a message from client " + list(addr.keys())[list(addr.values()).index(address[1])] + ", and the content is '" + data_divided[0] + "', the terminal is " + data_divided[1])    
    
    #data_divided[0]是信息，data_divided[1]是发信人的目标(1,2,3...)，address[1]是发信人的端口号   
    send = data_divided[0] + "^" + str(address[1])
    
    server.sendto(send.encode('utf-8'),(host,addr[data_divided[1][-1]]))

    
server.close()