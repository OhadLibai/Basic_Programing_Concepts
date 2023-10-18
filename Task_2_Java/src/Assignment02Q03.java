
public class Assignment02Q03 {

	public static void main(String[] args) {
		int numOfOdd = 2;
		int n = Integer.parseInt(args[0]);
		String fibstr= "1" + " " + "1";

		int prevprev=1;
		int prev=1;
		int current;
		int i=2;
		while (i<Integer.parseInt(args[0])){
			current= prev + prevprev;
			if (current%2 == 1) {
				numOfOdd++;
			}
			fibstr+= " "+current;
			prevprev=prev;
			prev=current;
			i++;
		}

		System.out.println("The first "+ n +" Fibonacci numbers are:" + fibstr);

		System.out.println("The number of odd numbers is: "+numOfOdd);

	}
}
