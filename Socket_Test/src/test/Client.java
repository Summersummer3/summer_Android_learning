package test;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.Socket;
import java.net.UnknownHostException;
import java.sql.Time;
import java.util.Scanner;

public class Client {
	private static Socket socket;
	private static String IP = "10.96.86.43";
	private static int PORT = 8888;
	private static Scanner scan;
	
	private static OutputStream out;
	private static BufferedWriter bw;
	private static InputStream in;
	private static BufferedReader br;
	private static String username;
	private static String msg;
	
	public static void main(String[] args) {
		try {
			int i = 0;
			
			socket = new Socket(IP,PORT);
			System.out.print("please enter your username:");
			scan = new Scanner(System.in);
			username = scan.nextLine();
			
			in = socket.getInputStream();
			br = new BufferedReader(new InputStreamReader(in));
			out = socket.getOutputStream();
			bw = new BufferedWriter(new OutputStreamWriter(out));
			bw.write(username+"\n");                   //server使用按行读取，则写入bufferedwriter时记得
//														每一行数据都要换行
			bw.flush();
			
			
			while(br.readLine().equals("0")){
				System.out.println("login fail, username doesn't exist!");
				System.out.print("please enter again：");
				scan = new Scanner(System.in);
				username = scan.nextLine();
				bw.write(username+"\n");  
				bw.flush();
				
			}

			
			while(i<5){
				try {
					Thread.currentThread();
					Thread.sleep(5000);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}


				bw.write("hello!!\n");
				bw.flush();
				i++;
				if((msg = br.readLine())!=null){
					System.out.println("<From server>"+msg);
				}
				}
			
			bw.write("bye\n");
			bw.close();
			out.close();
			socket.close();
			

		} catch (UnknownHostException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
	
	
}
