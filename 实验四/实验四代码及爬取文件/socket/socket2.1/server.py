import socket
import datetime
import time
import pymysql
 
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname() #获取本地主机名
port = 9999 #固定端口号
#绑定地址关键字，AF_INET下以元组的形式表示地址。常用bind((host,port))
serversocket.bind((host,port))

db = pymysql.connect(host='localhost', user='root', password='', 
		database='socket',cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()

#监听TCP，可以挂起的最大连接数
serversocket.listen(5)
while True:
  print('服务器启动，监听客户端链接')
  clientsocket,addr = serversocket.accept()  #被动接受TCP客户端的连接
  print('链接地址：%s' % str(addr))
  while True:
    try:
      data = clientsocket.recv(1024)  #接收数据
    except Exception:
      print('断开的客户端：',addr)
      break
    print('客户端发送内容：',data.decode('utf-8'))
    flag = 0
    if data.decode('utf-8') == "Time":
        cur = datetime.datetime.now().strftime('%F %T')
        reply = '当前时间为：' + cur
    elif data.decode('utf-8') == "Exit":
        reply = "Bye"
        flag = 1  
    elif data.decode('utf-8')[0:6] == "query:":
        str1 = data.decode('utf-8')[6:]
        print("client wants to query the info of "+str1)
        sql = "select student_name,student_gender from student where student_ID = "+str1
        cursor.execute(sql)
        if cursor.rowcount == 0:
            reply = 'Sorry, no such student, pls check.'
        for iter in cursor.fetchall():
            reply = '^%s^%s'% (iter["student_name"],iter["student_gender"])
    else:
        reply = input('回复：').strip()
        if not reply:
            break
    msg = time.strftime('%Y-%m-%d %X')#获取结构化时间戳
    msg1 = '[%s]:%s'% (msg,reply)
    clientsocket.send(msg1.encode('utf-8'))
    if flag == 1:
        break
  clientsocket.close()
serversocket.closel()