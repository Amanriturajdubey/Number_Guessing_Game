import java.net.DatagramSocket;
import java.net.DatagramPacket;

public class UDPServer{
    public static void main(String[] args)throws Exception{
        try{
        DatagramSocket server = new DatagramSocket(1234);
        byte[] recieveBuffer = new byte[1024];
        byte[] sendBuffer ;
        System.out.println("server is running");

        DatagramPacket recievePacket = new DatagramPacket(recieveBuffer,recieveBuffer.length);
        server.receive(recievePacket);
        
        String data = new String(recievePacket.getData(),0,recievePacket.getLength());
        System.out.println("data is :" + data);

        String[] numbers = data.split(",");
        int sum = 0;
        for(String num : numbers){
            sum += Integer.parseInt(num.trim());
        };
        System.out.println("the sum is:" + sum);

        String result = "sum is:" + sum;
        sendBuffer = result.getBytes();
        DatagramPacket sendPacket = new DatagramPacket(sendBuffer,sendBuffer.length,recievePacket.getAddress(),recievePacket.getPort());
        server.send(sendPacket);
        server.close();
        }catch(Exception e){
            e.printStackTrace();
        }
    }
}