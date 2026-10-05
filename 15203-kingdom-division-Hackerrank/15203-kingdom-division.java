import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    //static final boolean RED = true;
    //static final boolean BLACK = false;
    static final int SAME = 1;
    static final int DIFF = 0;
    static final long MEM = 1000000007;
    
    static List<Node> readyNodes = new LinkedList<>();
    
    static class Node {
        int name;
        List<Node> neighbors = new ArrayList<>();
        Node parent = null;
        boolean isDone = false;
        
        public Node(int name) {
            this.name = name;
        }
        
        boolean checkReady() {
            for (Node child : neighbors) {
                if (!child.isDone) {
                    return false;
                }
            }
            return true;
        }
    }
    
    static void rootTree(Node child, Node parent) {
        child.parent = parent;
        child.neighbors.remove(parent);
        for (Node superChild : child.neighbors) {
            rootTree(superChild, child);
        }
        if (child.neighbors.isEmpty()) {
            readyNodes.add(child);
        }
    }
    
    /*
    static long howMany(Node child, boolean color, boolean parentColor) { // Need DP here instead
        if (child.neighbors.isEmpty()) {
            if (color == parentColor)
                return 1;
            else
                return 0;
        }
        
        long[] redChildren = new long[child.neighbors.size()];
        long[] blackChildren = new long[child.neighbors.size()];
        
        long ways = 1;
        for (int i = 0; i < redChildren.length; i++) {
            redChildren[i] = howMany(child.neighbors.get(i), RED, color);
            blackChildren[i] = howMany(child.neighbors.get(i), BLACK, color);
            
            ways = (ways * (redChildren[i] + blackChildren[i])) % MEM;
        }
        
        if (color != parentColor) {
            long sub = 1;
            if (color == RED) {
                for (int i = 0; i < blackChildren.length; i++) {
                    sub = (sub * blackChildren[i]) % MEM;
                    if (sub == 0)
                        break;
                }
            }
            else {
                for (int i = 0; i < redChildren.length; i++) {
                    sub = (sub * redChildren[i]) % MEM;
                    if (sub == 0)
                        break;
                }
            }
            ways = (ways - sub + MEM) % MEM;
        }
        
        return ways;
    }*/

    static long kingdomDivision(int n, Node[] cities) {
        rootTree(cities[0], null);
        
        long[][] ways = new long[n][2]; //ways[nodeName][Diff/Same]
        for (Node leaf : readyNodes) {
            ways[leaf.name][SAME] = 1;
            ways[leaf.name][DIFF] = 0;
            leaf.isDone = true;
        }
        
        while (!readyNodes.isEmpty()) {
            List<Node> nextNodes = new LinkedList<>();
            for (Node done : readyNodes) {
                if (done.parent != null && done.parent.checkReady())
                    nextNodes.add(done.parent);
            }
            readyNodes = nextNodes;
            for (Node node : readyNodes) {
                long w = 1;
                for (Node child : node.neighbors) {
                    w = (w * (ways[child.name][SAME] + ways[child.name][DIFF])) % MEM;
                }
                ways[node.name][SAME] = w;
            
                long sub = 1;
                for (Node child : node.neighbors) {
                    sub = (sub * (ways[child.name][DIFF])) % MEM;
                    if (sub == 0)
                        break;
                }
                ways[node.name][DIFF] = (w - sub + MEM) % MEM;
                node.isDone = true;
            }
        }
        
        return (2*ways[0][DIFF]) % MEM;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        Node[] cities = new Node[n];
        for (int i = 0; i < n; i++) {
            cities[i] = new Node(i);
        }
        for(int i = 0; i < n-1; i++){
            int city1 = in.nextInt() - 1;
            int city2 = in.nextInt() - 1;
            cities[city1].neighbors.add(cities[city2]);
            cities[city2].neighbors.add(cities[city1]);
        }
        long result = kingdomDivision(n, cities);
        System.out.println(result);
        in.close();
    }
}


// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna