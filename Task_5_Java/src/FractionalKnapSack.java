package il.ac.tau.cs.sw1.ex7;
import java.util.*;

public class FractionalKnapSack implements Greedy<FractionalKnapSack.Item>{
    int capacity;
    double capacityToZero;
    List<Item> lst;

    FractionalKnapSack(int c, List<Item> lst1){
        capacity = c;
        capacityToZero = c;
        lst = lst1;
    }

    public static class Item {
        double weight, value, factor;
        Item(double w, double v) {
            weight = w;
            value = v;
            factor = v/w;
        }

        public double getFactor() {
            return this.factor;
        }

        @Override
        public String toString() {
            return "{" + "weight=" + weight + ", value=" + value + '}';
        }
    }

    @Override
    public Iterator<Item> selection() {
        // There are several ways to implement.
        // 3 of which is represented here, all of O(nlogn)


        //-->Using a TreeMap<--//

        /*
         SortedMap<Double, Item> doubleItemSortedMap = new TreeMap<>(Collections.reverseOrder());
        double num;
        for (Item item:this.lst) {
            num = item.value/item.weight;
            doubleItemSortedMap.put(num,item);
        }
        return doubleItemSortedMap.values().iterator();
        */


        //-->Using a TreeSet<--//

        /*
        Comparator<Item> suitedComparator = Comparator.comparing(Item::getFactor).reversed();
        SortedSet<Item> itemSortedSet = new TreeSet<>(suitedComparator);
        double num;
        for (Item item:this.lst) {
            itemSortedSet.add(item);
        }
        return itemSortedSet.iterator();
        */

        //--> Any of the map or set implementation can be implemented using Hash and then sorting on it //


        //-->Using a List<--//
        // (gets better results from running time performance aspect)

        Comparator<Item> suitedComparator = Comparator.comparing(Item::getFactor).reversed();
        this.lst.sort(suitedComparator);
        return this.lst.iterator();

    }

    @Override
    public boolean feasibility(List<Item> candidates_lst, Item element) {
        return capacityToZero > 0;
    }

    @Override
    public void assign(List<Item> candidates_lst, Item element) {
        if (capacityToZero-element.weight < 0) {
            double newWeight = capacityToZero;
            double newValue = (capacityToZero/element.weight) * element.value;
            Item finalItem = new Item(newWeight, newValue);
            candidates_lst.add(finalItem);
            capacityToZero -= element.weight;
        }
        else {
            candidates_lst.add(element);
            capacityToZero -= element.weight;
        }
    }


    @Override
    public boolean solution(List<Item> candidates_lst) {
        return sum(candidates_lst) == capacity;
    }

    private Double sum(List<Item> lst) {
        Double sum = 0.0;
        for (int i=0; i<lst.size(); i++) {
            sum += lst.get(i).weight;
        }
        return sum;
    }

}
