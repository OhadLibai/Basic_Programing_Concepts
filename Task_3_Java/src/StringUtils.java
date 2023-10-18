
public class StringUtils {

	public static String findSortedSequence(String str) {
		String[] strArr= str.split(" ");
		int L= strArr.length;
		int k=1;
		int j=1;
		int i=0;

		if (L==0) {
			return "";
		}

		String strtmp=strArr[0];
		String strfinal=strArr[0];


		while (i<L) {
			strtmp=strArr[i];
			k=1;
			while ( ((i+1)<L) && (checkLex(strArr[i], strArr[i+1])) ) {

				strtmp += " " +strArr[i+1];
				k++;
				i++;
			}
			if (k>=j) {
				strfinal=strtmp;
				j=k;
			}
			i++;
		}

		return strfinal;
	}


	public static boolean isEditDistanceOne(String a, String b) {
		int cnt=0, i=0;
		int L1= a.length();
		int L2=b.length();

		if (Math.abs(L1-L2)>=2) {
			return false;
		}
		//changed char below//
		if (L1==L2) {
			while (i<L1) {
				if (a.charAt(i) != b.charAt(i)) {
					cnt++;
					if (cnt==2) {
						return false;
					}
				}
				i++;
			}
			return true;
		}

		if (L2>L1) {
			return AddDelete(a,b);
		}
		else {
			return AddDelete(b,a);
		}

	}

	private static boolean checkLex( String str1, String str2) {
		int iterationsNum= Math.min(str1.length(),str2.length());

		for (int i=0; i<iterationsNum; i++) {
			if (str1.charAt(i)==str2.charAt(i))
				continue;

			if (str1.charAt(i)<str2.charAt(i))
				return true;

			else
				return false;
		}

		if (str2.length()>=str1.length())
			return true;
		else
			return false;
	}

	private static boolean AddDelete( String a, String b){
		//b.length>a.length//
		int i=0, j=0, cnt=0;
		int L1 = a.length();

		while (i<L1) {
			if (a.charAt(i) != b.charAt(j)) {
				cnt++;
				if (cnt ==2) {
					return false;
				}
				j++;
				continue;
			}
			i++;
			j++;
		}
		return true;
	}
}
