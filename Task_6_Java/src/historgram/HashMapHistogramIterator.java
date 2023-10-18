package il.ac.tau.cs.sw1.ex8.histogram;

import java.util.Set;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Iterator;
import java.util.TreeMap;
import java.util.HashMap;


/**************************************
 *  Add your code to this class !!!   *
 **************************************/

public class HashMapHistogramIterator<T extends Comparable<T>> 
							implements Iterator<Map.Entry<T, Integer>>{

	protected Iterator<Map.Entry<T,Integer>> sortedIterator;

		//option A
	public HashMapHistogramIterator(Set<Map.Entry<T,Integer>> entrySet) { //constructor 1
		entrySet.stream().sorted(Map.Entry.comparingByKey());
		this.sortedIterator = entrySet.iterator();
	}

		//option B
	public HashMapHistogramIterator(HashMap<T, Integer> hashMap) { //constructor 2
		TreeMap<T, Integer> treeMap = new TreeMap<T,Integer>(hashMap);
		this.sortedIterator = treeMap.entrySet().iterator();
	}

	
	@Override
	public boolean hasNext() {
		return sortedIterator.hasNext();
	}

	@Override
	public Map.Entry<T, Integer> next() {
		return sortedIterator.next();
	}

	@Override
	public void remove() {
		throw new UnsupportedOperationException();
		
	}
	
	//add private methods here, if needed
}
