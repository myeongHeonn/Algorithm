import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Node implements Comparable<Node>{
    int to;
    long cost;
    int time;
    
    public Node(int to, long cost, int time) {
        this.to = to;
        this.cost = cost;
        this.time = time;
    }

    @Override
    public int compareTo(Node o) {
        if (this.cost == o.cost) {
            return this.time - o.time;
        }
        
        return Long.compare(this.cost, o.cost);
    }
}

public class Main {
    
    static int MAX_V = 100_000;
    static long MAX_COST = 1_000_000_000_000L;
    static int MAX_TIME = 1_000_000_000;
    
    static ArrayList<Node>[] graph;
    static long[] cdist;
    static int[] tdist;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        
        graph = new ArrayList[MAX_V + 1];
        cdist = new long[MAX_V + 1];
        tdist = new int[MAX_V + 1];
        
        for (int i = 1; i <= MAX_V; i++) {
            graph[i] = new ArrayList<Node>();
            cdist[i] = MAX_COST;
            tdist[i] = MAX_TIME;
        }
        
        int busIndex = 1000;
        
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            
            long cost = Long.parseLong(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            
            int prev = -1;
            
            st = new StringTokenizer(br.readLine());
            
            for (int j = 0; j < m; j++) {
                busIndex++;
                int now = Integer.parseInt(st.nextToken());
                
                // 탑승
                graph[now].add(new Node(busIndex, cost, 0));
                
                // 하차
                graph[busIndex].add(new Node(now, 0, 0));
                
                // 이동
                if (prev != -1) {
                    graph[prev].add(new Node(busIndex, 0, 1));
                }
                
                prev = busIndex;
            }
        }
        
        dijkstra(A);
        
        System.out.println((cdist[B] == MAX_COST ? -1 : cdist[B]) + " " + (tdist[B] == MAX_TIME ? -1 : tdist[B]));

    }
    
    static void dijkstra(int start) {
        PriorityQueue<Node> pq = new PriorityQueue<Node>();
        pq.add(new Node(start, 0, 0));
        cdist[start] = 0;
        tdist[start] = 0;
        
        while (!pq.isEmpty()) {
            Node now = pq.poll();
            
            if (now.cost > cdist[now.to]) continue;
            if (now.cost == cdist[now.to] && now.time > tdist[now.to]) continue;
            
            for (Node next : graph[now.to]) {
                long newCost = now.cost + next.cost;
                int newTime = now.time + next.time;
                
                if (newCost < cdist[next.to]) {
                    cdist[next.to] = newCost;
                    tdist[next.to] = newTime;
                    pq.add(new Node(next.to, newCost, newTime));
                }
                else if (newCost == cdist[next.to] && newTime < tdist[next.to]) {
                    tdist[next.to] = newTime;
                    pq.add(new Node(next.to, newCost, newTime));
                }
            }
        }
    }
}