package il.ac.tau.cs.sw1.hw6;

import java.util.Arrays;

public class Polynomial {
	private int degree;
	private double[] coefficients;

	/*
	 * Creates the zero-polynomial with p(x) = 0 for all x.
	 */
	public Polynomial() {
		degree = 0;
		coefficients = new double[]{0};
	}


	/*
	 * Creates a new polynomial with the given coefficients.
	 */

	public Polynomial(double[] coefficients) {
		this.coefficients = coefficients;
		this.degree = coefficients.length-1;
	}


	/*
	 * Addes this polynomial to the given one
	 *  and retruns the sum as a new polynomial.
	 */

	public Polynomial adds(Polynomial polynomial) {
		int maxDegree = Math.max(polynomial.degree, this.degree);
		double[] newCoefficents = new double[maxDegree+1];


		/*just mentioning that it is possible to avoid from duplicating the 2 loops and write a specific function,
		once we know who of the 2 polynom has larger degree*/

		int i=0;
		if (maxDegree==this.degree) {
			while (i <= polynomial.degree ) {
				newCoefficents[i] = polynomial.coefficients[i] + this.coefficients[i];
				i++;
			}
			for (int j=i+1 ; j<=this.degree; j++) { //loop for the rest//
				newCoefficents[j] = this.coefficients[j];
			}
		}

		else {
			while (i <= this.degree) { //symetrical to the loop above//
				newCoefficents[i] = polynomial.coefficients[i] + this.coefficients[i];
				i++;
			}
			for (int j=i+1 ; j<=polynomial.degree ; j++) {
				newCoefficents[j] = polynomial.coefficients[j];
			}
		}

		Polynomial createPolynomial = new Polynomial(newCoefficents);
		return createPolynomial;
	}


	/*
	 * Multiplies a to this polynomial and returns 
	 * the result as a new polynomial.
	 */

	public Polynomial multiply(double a) {
		double[] newCoefficients = Arrays.copyOf(coefficients,coefficients.length);
		Polynomial createPolynom = new Polynomial(newCoefficients);
		for (int i=0; i<=createPolynom.degree; i++) {
			createPolynom.coefficients[i] *= a;
		}
		return createPolynom;
	}


	/*
	 * Returns the degree (the largest exponent) of this polynomial.
	 */

	public int getDegree() {
		return this.degree;
	}


	/*
	 * Returns the coefficient of the variable x 
	 * with degree n in this polynomial.
	 */

	public double getCoefficient(int n){
		return this.coefficients[n];
	}


	/*
	 * set the coefficient of the variable x 
	 * with degree n to c in this polynomial.
	 * If the degree of this polynomial < n, it means that the coefficient of the variable x
	 * with degree n was 0, and now it will change to c. 
	 */

	public void setCoefficient(int n, double c) {
		if (this.degree>=n)
			this.coefficients[n] = c;

		else {
			double[] newCoefficients = new double[n+1];
			System.arraycopy(this.coefficients,0,newCoefficients,0,this.degree);
			newCoefficients[n] = c;
			this.coefficients = newCoefficients;
		}
	}


	/*
	 * Returns the first derivation of this polynomial.
	 *  The first derivation of a polynomal a0x0 + ...  + anxn is defined as 1 * a1x0 + ... + n anxn-1.
	 */

	public Polynomial getFirstDerivation() {
		//coefficent of index 0 is gone and n-->n-1//
		Polynomial createPolynom = new Polynomial();
		double[] newCoefficients = new double[this.coefficients.length-1];
		int k=1;
		for (int i=0 ; i<newCoefficients.length; i++) {
			newCoefficients[i] = this.coefficients[k] * k;
			k++;
		}

		createPolynom.coefficients = newCoefficients;
		createPolynom.degree = createPolynom.coefficients.length-1;
		return createPolynom;
	}


	/*
	 * given an assignment for the variable x,
	 * compute the polynomial value
	 */

	public double computePolynomial(double x) {
		double res = 0;
		for (int i=0; i<this.coefficients.length; i++) {
			res += (Math.pow(x,i)*coefficients[i]);
		}
		return res;
	}


	/*
	 * given an assignment for the variable x,
	 * return true iff x is an extrema point (local minimum or local maximum of this polynomial)
	 * x is an extrema point if and only if The value of first derivation of a polynomal at x is 0
	 * and the second derivation of a polynomal value at x is not 0.
	 */

	public boolean isExtrema(double x) {
		Polynomial firstDerivation = this.getFirstDerivation();
		if (firstDerivation.computePolynomial(x) == 0.0) {
			Polynomial secondDerivation = firstDerivation.getFirstDerivation();
			if (secondDerivation.computePolynomial(x) == 0.0) {
				return true;
			}
		}

		return false;
	}

}
