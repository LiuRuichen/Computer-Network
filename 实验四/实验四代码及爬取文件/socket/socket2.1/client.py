import socket
  
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
s.connect((host,port)) #初始化服务器连接
while True:   
    flag = 0
    data = input('>>').strip()
    if not data:
        break
    elif data[0:6] == "query:":   
        flag = 1
    s.send(data.encode('utf-8'))
    
    msg = s.recv(1024)  #接收数据
    msg_decode = msg.decode('utf-8')
    
    if msg_decode[-3:] == "Bye":
        print(msg_decode[-3:])
        break       
    elif flag == 1:
        if msg_decode[-34:] == "Sorry, no such student, pls check.":
            print(msg_decode)
        else:
            msg_divided = msg_decode.split("^",2)
            tag = msg_divided[0]
            msg1 = msg_divided[1]
            msg2 = msg_divided[2] 
            print(tag+"The name of the student is "+msg1+", while the gender of the student is "+msg2)
    else:
        print("服务端回应: "+msg.decode('utf-8'))
               
s.close()