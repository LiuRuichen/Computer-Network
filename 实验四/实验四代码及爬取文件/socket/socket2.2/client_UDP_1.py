import socket
#创建Socket时， SOCK_DGRAM 指定了这个Socket的类型是UDP。
client = socket.socket(type = socket.SOCK_DGRAM)

host = socket.gethostname()
client.sendto("info".encode('utf-8'),(host,9999))
re_Data,address = client.recvfrom(1024)
msg_divided = re_Data.decode('utf-8').split("&",4)

dic = {}
i = 0
for i in range(0,4):
    strl = msg_divided[i]
    
    str_divided = strl.split('^')
    
    print(str_divided[0]+", his port is "+str_divided[1])
    
    dic[str_divided[0]] = int(str_divided[1])
    
    
while True:
    
    flag = 0
    re_Data,address = client.recvfrom(1024)
    re_Data = re_Data.decode('utf-8')
        
    if re_Data:
        re_divided = re_Data.split('^')
        
        print("来自" + list(dic.keys())[list(dic.values()).index(int(re_divided[1]))] + "的信息:" + re_divided[0])
        if re_divided[0] == "Exit":
            send_data = "Bye"
            print("Chat is over")
            flag = 1
        elif re_divided[0] == "Bye":
            break
        else:
            send_data = input('>>').strip()
        info = send_data + "/" + list(dic.keys())[list(dic.values()).index(int(re_divided[1]))] 
        client.sendto(info.encode('utf-8'),(host,9999))
        if flag == 1:
            break
        
    else:
        print("pls select a friend to communicate:") 
        selection = input('')
        while True:
            if selection != "1" and selection != "2" and selection != "3" and selection != "4":
                print("error input, pls check")
                selection = input('')
            else:
                break
                
        send_data = input('>>').strip()
        info = send_data + "/" + selection 
        client.sendto(info.encode('utf-8'),(host,9999))
            
        
client.close()