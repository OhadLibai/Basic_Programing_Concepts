

public class Assignment1 {
	public static void main(String[] args){
		int temp1 = args[0].charAt(0);
		int temp2= temp1+Integer.parseInt(args[1]);
		char newChar = (char)temp2;
		System.out.println("New char is "+ newChar +".");
		//System.out.println("New char is " + newChar + ".");
	}
}
