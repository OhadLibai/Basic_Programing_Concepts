package il.ac.tau.cs.sw1.riddle.a;

public class A {
	
	private B b;
	
	public A(B b) {
		this.b = b;
	}

	public void printA() {
		System.out.println("A1");
		int i = b.getIPlus();
		i -=1;
		System.out.println(i);
		System.out.println("A2");
	}
}
