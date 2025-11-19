import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.Scanner;

public class UDPClient{
    public static void main(String[] args)throws Exception{
        try{
            DatagramSocket client = new DatagramSocket();
            InetAddress serverIP = InetAddress.getByName("localhost");
            Scanner sc = new Scanner(System.in);
            System.out.println("enter the number saprated by comma (,):");
            String input = sc.nextLine();

            byte[] sendBuffer = new byte[1024];
            DatagramPacket sendPacket = new DatagramPacket(sendBuffer,sendBuffer.length,serverIP,1234);
            client.send(sendPacket);

            byte[] recieveBuffer = new byte[1024];
            DatagramPacket recievePacket = new DatagramPacket(recieveBuffer,recieveBuffer.length);
            client.receive(recievePacket);

            String response = new String(recievePacket.getData(),0,recievePacket.getLength());
            System.out.println("data is : " + response);
            client.close();
        }catch(Exception e){
            e.printStackTrace();
        }
    }
}