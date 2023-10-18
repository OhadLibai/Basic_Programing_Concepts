

public class Assignment02Q02 {

	public static void main(String[] args) {
		// do not change this part below
		double piEstimation = 0.0;

		int Sn = -1;
		int sign= -1;
		double sum=0;
		double frac;
		int i=0;
		while ( i <Integer.parseInt(args[0])) {
			Sn+=2;
			frac = (double) 1/Sn ;
			sign = ((-1)*sign);
			sum +=  (sign*frac) ;
			i++;
		}
		piEstimation= 4*sum;

		// do not change this part below
		System.out.println(piEstimation + " " + Math.PI);

	}

}
