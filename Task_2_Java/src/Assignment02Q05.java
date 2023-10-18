import java.util.Arrays;

public class Assignment02Q05 {

	public static void main(String[] args) {
		// do not change this part below
		int N = Integer.parseInt(args[0]);
		int[][] matrix = new int[N][N]; // the input matrix to be
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				matrix[i][j] = Integer.parseInt(args[1 + (i * N) + j]); // the value at [i][j] is the i*N+j item in args (without considering args[0])
			}
		}
		for (int i = 0; i < N; i++)
			System.out.println(Arrays.toString(matrix[i]));

		System.out.println("");

		int[][] rotatedMatrix = new int[N][N]; // the rotated matrix
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				rotatedMatrix[i][j] = Integer.parseInt(args[1 + (i * N) + j]);
			}
		}

		int cnt=0;
		int midDiag= Math.floorDiv(N,2);
		while (cnt < midDiag) {

			//first row//
			for (int i = 0; (i+2*cnt) < N; i++) {
				rotatedMatrix[0+cnt][i+cnt] = matrix[N - 1 - i - cnt][0+cnt];
			}

			//last column//
			for (int i = 0; (i+2*cnt) < N; i++) {
				rotatedMatrix[i+cnt][N - 1-cnt] = matrix[0+cnt][i+cnt];
			}

			//last row//
			for (int i = 0; (i+2*cnt) < N; i++) {
				rotatedMatrix[N - 1-cnt][N - 1 - i-cnt] = matrix[i+cnt][N - 1-cnt];
			}

			//first column//
			for (int i = 0; (i+2*cnt) < N; i++) {
				rotatedMatrix[N - 1 - i-cnt][0+cnt] = matrix[N - 1-cnt][N - 1 - i-cnt];
			}
			cnt++;
		}


		// do not change this part below
		for (int i = 0; i < N; i++) {
			System.out.println(Arrays.toString(rotatedMatrix[i])); // this would compile after you would put value in transposedMatrix
		}
	}
}
