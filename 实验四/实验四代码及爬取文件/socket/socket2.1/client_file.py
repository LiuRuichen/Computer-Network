import socket
import os

    
while True:
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostname() 
    
    port = 9999
    #tcp_socket.bind((host,port))
    # 连接服务器
    tcp_socket.connect((host,port))    
    print("Pls select an opreation:")
    a = input('')    
    if a == "Exit":
        tcp_socket.send("Exit".encode())
        mes = tcp_socket.recv(1024)
        print(mes.decode())
        tcp_socket.close()
        break
       
    elif a == "ls":  
        tcp_socket.send(a.encode('utf-8'))
        mes = tcp_socket.recv(1024).decode()
        arr = mes.split('^')
        arr1 = arr[:-1]
        for r in arr1:
            print(r)
    elif a == "download":
            
        # 输入要下载的文件名
        file_name = input("请输入要下载的文件名:")
 
        # 将文件名发送至服务器端
        tcp_socket.send(file_name.encode('utf-8'))
        # 创建一个空文件
        #new_file = open(file_name, "wb")
        # 用与计算读取的字节数
        i = 0
        # 接收服务器端返回的内容
        mes = tcp_socket.recv(1024)
        if mes.decode("utf8","ignore") == "No such file":
            print("No such file")
        elif mes.decode("utf8","ignore") == "Bye":
            print("Bye")
        else:
            filesize = mes.decode()
            ifilesize = int(filesize)
            count = int(ifilesize/1024)
            if ifilesize % 1024 > 0:
                count = count + 1
            
            print("你想使用默认文件名称吗？y/n")
            tg = input('')
            if tg == 'y':
                with open('./[new]' + file_name, 'wb') as f:
                    for i in range(0,count):
                        mes = tcp_socket.recv(1024)
                        f.write(mes)
                    f.close()
            else:
                f_name = input("请输入文件名称:")
                with open('./' + f_name, 'wb') as f:
                    for i in range(0,count):
                        mes = tcp_socket.recv(1024)
                        f.write(mes)
                    f.close()
                
    
        
            print("文件下载成功！")
            print("您所要下载的文件是 " + file_name)
            if tg == 'y':
                size = os.path.getsize('./[new]' + file_name)
            else:
                size = os.path.getsize('./' + f_name)
            print("本次下载共计"+str(size/1024)+"KB")
            # 关闭套接字
            tcp_socket.close()
    else:
        print("wrong operation, pls check.")
            
tcp_socket.close()
