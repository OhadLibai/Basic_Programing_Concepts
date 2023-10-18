package il.ac.tau.cs.sw1.ex7;
import java.util.*;


public class Graph implements Greedy<Graph.Edge>{
    List<Edge> lst; //Graph is represented in Edge-List. It is undirected. Assumed to be connected.
    int n; //nodes are in [0,..., n]
    int[] parents;
    int[] rank;

    Graph(int n1, List<Edge> lst1){
        lst = lst1;
        n = n1;
        rank = new int[n1];
        parents = new int[n1];
        Arrays.fill(parents,-1);
    }

    public static class Edge{
        int node1, node2;
        double weight;

        Edge(int n1, int n2, double w) {
            node1 = n1;
            node2 = n2;
            weight = w;
        }

        public Double getWeight() {
            return this.weight;
        }

        public int getNode1() {
            return this.node1;
        }

        public int getNode2() {
            return this.node2;
        }

        @Override
        public String toString() {
            return "{" + "(" + node1 + "," + node2 + "), weight=" + weight + '}';
        }
    }

    @Override
    public Iterator<Edge> selection() {
        // Like the previous execrsice - plenty of room to implement here //

        // List method with the aid of accessor methods //
        /*
        Comparator<Edge> suitedComparator =
                Comparator.comparing(Edge::getWeight).thenComparing(Edge::getNode1).thenComparing(Edge::getNode2);

        this.lst.sort(suitedComparator);
        return this.lst.iterator();
        */



        // Another option :

        Comparator<Edge> suitedComparator =
                Comparator.comparing((Edge e)->e.weight).thenComparing(e -> e.node1).thenComparing(e -> e.node2);

        this.lst.sort(suitedComparator);
        return this.lst.iterator();
    }

    @Override
    public boolean feasibility(List<Edge> candidates_lst, Edge element) {
        //check if adding an edge results in circle
        //(union-find approach)

        int node1Parent = getAbsoluteParent(this.parents, element.node1);
        int node2Parent = getAbsoluteParent(this.parents, element.node2);
        return (!(node1Parent == node2Parent));
    }

    @Override
    public void assign(List<Edge> candidates_lst, Edge element) {
        //(union-find approach)

        int node1Parent = getAbsoluteParent(this.parents, element.node1);
        int node2Parent = getAbsoluteParent(this.parents, element.node2);
        int rankNode1 = this.rank[node1Parent];
        int rankNode2 = this.rank[node2Parent];

        if (rankNode1 > rankNode2) {
            this.parents[node2Parent] = node1Parent;
        }

        else {
            this.parents[node1Parent] = node2Parent;
            if (rankNode1 == rankNode2) {
                this.rank[node2Parent] += 1;
            }
        }

        candidates_lst.add(element);
    }

    @Override
    public boolean solution(List<Edge> candidates_lst) {
        return ((this.n-1) == candidates_lst.size());
    }


    public int getAbsoluteParent(int[] parents, int node) {
        //base case//
        if (parents[node] == -1)
            return node;

        else
            return getAbsoluteParent(parents, parents[node]);
    }

}
