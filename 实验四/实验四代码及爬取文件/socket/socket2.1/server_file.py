import socket
import os
 
def file_send(file_name,client_socket):
    
    path = os.getcwd()
    ct = 0
    for filename in os.listdir(path):
        if filename == file_name:
            filesize = os.path.getsize(file_name)
            sfilesize = '%d'%filesize
            client_socket.send(sfilesize.encode())
            with open (file_name,"rb") as f:
                while True:
                    file_content = f.read(1024)
                    if file_content:
                        client_socket.send(file_content)
                    else:
                        break
            ct = 1  
            break
    if ct == 0:
        print("No such file")
        client_socket.send(b'No such file')

def main():
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 固定端口号
    host = socket.gethostname() 
    port = 9999
    tcp_socket.bind((host,port))
    
    # 将主动套接字转为被动套接字
    tcp_socket.listen(128)
    print("等待连接...")
    
    while True: 
        print('服务器启动，监听客户端链接')
        # 利用accept获取分套接字以及客户端的地址
        client_socket,client_addr = tcp_socket.accept()
        # 接收客户端的数据
        file_name = client_socket.recv(1024)
        
        if file_name.decode() == "Exit":
            print(file_name.decode())
            client_socket.send("Bye".encode())
            break
        elif file_name.decode() == 'ls':
            path = os.getcwd()
            
            w = ""
            for filename in os.listdir(path):
                print(filename)
                w = w + filename + '^'
               
            client_socket.send(w.encode())
        else:
            print(file_name.decode())
            file_send(file_name.decode(),client_socket)
        
    client_socket.close()
            
if __name__ == "__main__":
    main()