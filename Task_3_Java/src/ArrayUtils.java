import java.util.Arrays;

public class ArrayUtils {

	public static int[] shiftArrayCyclic(int[] array, int move, char direction) {
		int L = array.length;
		int[] arr = Arrays.copyOf(array, L);
		int absMove= Math.abs(move);

		if  ( (direction != 'R' && direction!='L') || (move==0) )
			return array;

		if ( ((direction == 'R') && (move > 0)) || ((direction == 'L') && (move < 0)) ) {       //positive direction
			for (int i = 0; i < L ; i++) {
				array[(i+absMove) % L] = arr[i];
			}
			return array;
		}

		else {                                   //negetive direction
			for (int i = 0; i < L ; i++) {
				array[i] = arr[(i+absMove)%L];
			}
			return array;
		}
	}


	public static int findShortestPath(int[][] m, int i, int j) {
		int cnt=0;
		int minpath= m.length+1 ;
		if (i==j)
			return 0;

		int shortestPath= recursiveShort(m, i, j, cnt, minpath);
		if (shortestPath==m.length+1)
			return -1;
		else
			return shortestPath;
	}

	private static int recursiveShort(int[][] m, int i, int j, int cnt, int minpath) {
		int l=0;
		while (l<m.length) {
			//base case//
			if (m[i][j]==1) {
				cnt++;
				return cnt;
			}

			if (m[i][l] == 1) {
				cnt= recursiveShort(m, l , j, cnt, minpath) + 1;
			}
			if (cnt>0) {
				if (minpath>cnt) {
					minpath=cnt;
				}
			}
			cnt=0;
			l++;
		}

		return minpath;
	}

}
