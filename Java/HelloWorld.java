package practice;
import java.util.Scanner;


public class HelloWorld {
	public static void main(String[] args) {
		Scanner scanner=new Scanner(System.in);
		
		System.out.println("What is your name?");
		String goodName=scanner.nextLine();
		
		System.out.println("Hello " + goodName + "!");
		
	}
}

