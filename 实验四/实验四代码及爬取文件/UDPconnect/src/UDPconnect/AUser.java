package UDPconnect;
//client A
import java.io.*;
import java.net.*;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
//窗口
public class AUser extends JFrame{
    JTextArea mainArea;
    JTextArea sendArea;
    JButton sendBtn;
    JButton exitBtn;
    AUserChat UserChat;

    public void setAUserChat(AUserChat userchat) {
        this.UserChat = userchat;
    }
    //构造方法
    public AUser(){
        super("client A");
        Container contain=getContentPane();
        //contain.setLayout(new BorderLayout());
        contain.setLayout(new BorderLayout(3,3));
        mainArea=new JTextArea();
        //背景图片
        Image image1 = new ImageIcon("src/sok.jpg").getImage();
        mainArea=new JTextArea() {
            Image image2 = image1;
            Image grayImage = GrayFilter.createDisabledImage(image2);
            {
                setOpaque(false);
            }

            public void paint(Graphics g) {
                super.paintComponent(g);
                Dimension size=this.getParent().getSize();
                g.drawImage(image2,0,0,size.width,size.height,null);
                //g.drawImage(image2, 0, 0, this);
                super.paint(g);
            }
        };
        mainArea.setEditable(true);
        mainArea.setOpaque(false);
        //构造滚动组件并使之透明
        JScrollPane Scroll=new JScrollPane(mainArea);
        Scroll=new JScrollPane(mainArea);
        Scroll.setOpaque(false);
        Scroll.getViewport().setOpaque(false);
        //滚动条功能实现
        Scroll.setBorder(BorderFactory.createTitledBorder("chat history"));
        JPanel panel=new JPanel();
        panel.setLayout(new BorderLayout());
        sendArea=new JTextArea(3,8);
        JScrollPane sendScroll=new JScrollPane(sendArea);
        UserChat=new AUserChat(this);
        UserChat.start();
        sendBtn=new JButton("send");
        //事件处理
        sendBtn.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                UserChat.sendMsg(sendArea.getText().trim());
                mainArea.append("[clientA]"+sendArea.getText().trim()+"\n");
                sendArea.setText("");
            }
        });
        exitBtn=new JButton("exit");
        exitBtn.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                System.exit(0);
            }
        });
        JPanel tmpPanel=new JPanel();
        tmpPanel.add(sendBtn);
        JPanel tmpPanel2=new JPanel();
        tmpPanel2.add(exitBtn);
        panel.add(tmpPanel,BorderLayout.EAST);
        panel.add(tmpPanel2,BorderLayout.WEST);
        panel.add(sendScroll,BorderLayout.CENTER);
        contain.add(Scroll,BorderLayout.CENTER);
        contain.add(panel,BorderLayout.SOUTH);
        setSize(500,300);
        setVisible(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
    //主方法
    public static void main(String []args){
        AUser ui=new AUser();
    }
    //线程
    class AUserChat extends Thread{
        AUser ui;
        AUserChat(AUser ui){
            this.ui=ui;
            ui.setAUserChat(this);
        }
        //重写run
        public void run(){
            //接收数据包
            String s=null;
            DatagramSocket client=null;
            DatagramPacket pack=null;
            byte data[]=new byte[10000];
            pack=new DatagramPacket(data,data.length);
            try {
                client=new DatagramSocket(8888);
            } catch (SocketException e) {
                e.printStackTrace();
            }
            while(true){
                if(client==null)
                    break;
                else{
                    try {
                        client.receive(pack);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                    String msg=new String(pack.getData(),0,pack.getLength());
                    ui.mainArea.append("[clientB]:"+msg+"\n");
                }
            }
        }
        public void sendMsg(String s){//发送数据包
            byte buffer[]=s.getBytes();
            try {
                InetAddress add=InetAddress.getByName("localhost");
                DatagramPacket data = new DatagramPacket(buffer,buffer.length,add,7777);
                DatagramSocket client = new DatagramSocket();
                client.send(data);
            } catch (UnknownHostException e) {
                e.printStackTrace();
            }catch (SocketException e) {
                e.printStackTrace();
            }catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

}

