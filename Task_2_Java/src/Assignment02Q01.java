
public class Assignment02Q01 {

	public static void main(String[] args) {
		for (String st :args) {
			if ( (st.charAt(0)%5) == 0 )
				System.out.println(st.charAt(0));
		}
	}
}
