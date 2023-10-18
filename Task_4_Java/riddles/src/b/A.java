package il.ac.tau.cs.sw1.riddle.b;

/**
 * Complete the code of A's methods without changing B and C.
 */
public class A {

	private B b;

	public A(B b) {
		this.b = b;
	}

	public static void printA(B b) { //s1//
		new B(b, " #no matter what's written here# ");
	}

	public void printA2() { //s2//
		B.foo(this.b);
	}

	public static void printA3(A a) { //s3//
		a.b.methodB(a.b);
	}
	
}
