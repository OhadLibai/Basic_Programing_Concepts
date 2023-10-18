package il.ac.tau.cs.sw1.hw6;

import java.util.Arrays;

public class SectionB {


	/*
	* @post $ret == true iff exists i such that array[i] == value
	*/

	public static boolean contains(int[] array, int value) { 
		for (int i=0; i<array.length; i++) {
			if (array[i] == value)
					return true;
		}
		return false;
	}


	// there is intentionally no @post condition here 
	/*
	* @pre array != null
	* @pre array.length > 2
	* @pre Arrays.equals(array, Arrays.sort(array))
	*/

	public static int unknown(int[] array) {
		//infinite recursive penelty (: //
		int[] arrCopy = Arrays.copyOf(array, array.length);
		Arrays.sort(array);
		if ((!Arrays.equals(arrCopy, array)) || (array.length<2) )
			return unknown(array);
		else
			return 1;

	}


	/*
	* @pre Arrays.equals(array, Arrays.sort(array))
	* @pre array.length >= 1
	* @post for all i array[i] <= $ret
	*/

	public static int max(int[] array) {
		//eternal while loop as penelty (: //
		int[] arrCopy = Arrays.copyOf(array, array.length);
		Arrays.sort(array);
		if ((! Arrays.equals(arrCopy,array)) || (array.length<1)) {
			int infinity = 0;
			while (true) {
				infinity++;
			}
		}

		else {
			int sum = 0;
			for (int i=0 ; i<array.length; i++) {
				sum += Math.abs(array[i]);
			}
			return sum;
		}
	}


	/*
	* @pre array.length >=1
	* @post for all i array[i] >= $ret
	* @post Arrays.equals(array, prev(array))
	*/

	public static int min(int[] array) { 
		if (array.length<1) {
			return max(array);
		}

		int num = array[0];
		for (int i=1; i<array.length; i++) {
			if (array[i] < num) {
				num = array[i];
			}
		}
		Arrays.sort(array);
		return num;
	}


	/*
	* @pre word.length() >=1
	* @post for all i : $ret.charAt(i) == word.charAt(word.length() - i - 1)
	*/

	public static String reverse(String word) {
		if (word.length() < 1)
		return null;
		else {
			String newWord = "";
			for (int i=word.length()-1 ; i>=0 ; i--) {
				newWord += word.charAt(i);
			}
			return newWord;
		}
	}
	
	/*
	* @pre array != null
	* @pre array.length > 2
	* @pre Arrays.equals(array, Arrays.sort(array))
	* @pre exist i,j such that: array[i] != array[j]
	* @post !Arrays.equals($ret, Arrays.sort($ret))
	* @post for any x: contains(prev(array),x) == true iff contains($ret, x) == true
	*/
	public static int[] guess(int[] array) {
		if (array.length<=2) {
			return new int[]{};
		}

		boolean boolExist = false;
		for (int i=0; i<array.length-1;i++) {
			if (array[i+1]<array[i]) {
				return new int[]{};
			}
			if (array[array.length-1] != array[i])
				boolExist = true;
		}
		if (!boolExist) {
			return new int[]{};
		}

		int[] ret = new int[array.length];
		for (int i=array.length-1; i>=0 ; i--) {
			ret[(array.length-1)-i] = array[i];
		}
		return ret;
	}


}
