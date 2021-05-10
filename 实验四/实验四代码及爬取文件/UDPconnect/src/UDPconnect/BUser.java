package UDPconnect;
//client B
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;
import java.net.*;


import java.awt.BorderLayout;
import java.awt.Graphics;

import javax.swing.*;



import UDPconnect.AUser.AUserChat;

public class BUser extends JFrame{
    JTextArea mainArea = null;
    private JTextArea sendArea = null;
    private JScrollPane Scroll = null;
    private JButton sendBtn = null;
    private JButton exitBtn = null;
    private ImageIcon image = null;
    BUserChat UserChat;
    public void setBUserChat(BUserChat userchat) {
        this.UserChat = userchat;
    }
    //构造方法
    public BUser(){
        super("client B");
        Container contain=getContentPane();
        contain.setLayout(new BorderLayout(3,3));
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
        Scroll=new JScrollPane(mainArea);
        Scroll.setOpaque(false);
        Scroll.getViewport().setOpaque(false);

        //历史记录部分的滚动条功能实现
        Scroll.setBorder(BorderFactory.createTitledBorder("chat history"));
        setVisible(true);
        //输入框部分
        JPanel panel=new JPanel();
        panel.setLayout(new BorderLayout());
        panel.setBackground(null);
        panel.setOpaque(false);

        //设置大小
        sendArea=new JTextArea(3,8);
        //输入框部分需要滚动条功能
        JScrollPane sendScroll=new JScrollPane(sendArea);
        UserChat=new BUserChat(this);
        //开始发送信息
        UserChat.start();
        sendBtn=new JButton("send");
        //事件处理
        sendBtn.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                UserChat.sendMsg(sendArea.getText().trim());
                mainArea.append("[clientB]"+sendArea.getText().trim()+"\n");
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
        BUser ui=new BUser();
    }
}

//线程
class BUserChat extends Thread{
    BUser ui;
    BUserChat(BUser ui){
        this.ui=ui;
        ui.setBUserChat(this);
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
            client=new DatagramSocket(7777);
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
                ui.mainArea.append("[clientA]:"+msg+"\n");
            }
        }
    }
    public void sendMsg(String s){//发送数据包
        byte buffer[]=s.getBytes();
        try {
            InetAddress add=InetAddress.getByName("localhost");
            DatagramPacket data=new DatagramPacket(buffer,buffer.length,add,8888);
            DatagramSocket client=new DatagramSocket();
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

