package il.ac.tau.cs.sw1.ex8.histogram;

import java.util.Collection;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;
import java.util.HashMap;
import java.util.TreeMap;


/**************************************
 *  Add your code to this class !!!   *
 **************************************/
public class HashMapHistogram<T extends Comparable<T>> implements IHistogram<T>{

	protected HashMap<T, Integer> hashMap;

	public HashMapHistogram() {
		this.hashMap = new HashMap<T, Integer>();
	}


	@Override
	public void addItem(T item) {
		if (! hashMap.containsKey(item))
			hashMap.put(item, 1);
		else
			this.hashMap.replace(item, hashMap.get(item), hashMap.get(item)+1);
	}
	
	@Override
	public boolean removeItem(T item)  {
		boolean exist = this.hashMap.replace(item, hashMap.get(item), hashMap.get(item)-1);
		if (exist && hashMap.get(item) == 0) {
			hashMap.remove(item);
		}
		return exist;
	}
	
	@Override
	public void addAll(Collection<T> items) {
		for(T t:items) {
			this.addItem(t);
		}
	}

	@Override
	public int getCountForItem(T item) {
		if (hashMap.containsKey(item))
			return hashMap.get(item);
		else
			return 0;
	}

	@Override
	public void clear() {
		hashMap.clear();
	}

	@Override
	public Set<T> getItemsSet() {
		return hashMap.keySet();
	}
	
	@Override
	public int getCountsSum() {
		Collection<Integer> values = hashMap.values();
		int cnt = 0;
		for (Integer integer:values) {
			cnt += (int) integer;
		}
		return cnt;
	}

	@Override
	public Iterator<Map.Entry<T, Integer>> iterator() {

		//constructor 2 - option B//
		//Iterator<Map.Entry<T,Integer>> hashMapHistIt = new HashMapHistogramIterator<>(this.hashMap);
		//return hashMapHistIt;

		//constructor 1 - option A//
		Iterator<Map.Entry<T, Integer>> hashMapHistIt = new HashMapHistogramIterator<>(this.hashMap.entrySet());
		return hashMapHistIt;
	}
	
	//add private methods here, if needed
}
