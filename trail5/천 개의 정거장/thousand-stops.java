import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Node implements Comparable<Node> {
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
            return Integer.compare(this.time, o.time);
        }
        return Long.compare(this.cost, o.cost);
    }
}

public class Main {
    
    static final long COST_INF = 1_000_000_000_000L;
    static final int TIME_INF = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());

        List<List<Node>> graph = new ArrayList<>();
        
        for (int i = 0; i <= 1000; i++) {
            graph.add(new ArrayList<>());
        }
        
        int virtualNodeIdx = 1000;

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            long cost = Long.parseLong(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            
            int prevVirtualNode = -1;
            
            for (int j = 0; j < m; j++) {
                int station = Integer.parseInt(st.nextToken());
                
                virtualNodeIdx++;
                graph.add(new ArrayList<>()); 

                graph.get(station).add(new Node(virtualNodeIdx, cost, 0));
                
                graph.get(virtualNodeIdx).add(new Node(station, 0, 0));
                
                if (prevVirtualNode != -1) {
                    graph.get(prevVirtualNode).add(new Node(virtualNodeIdx, 0, 1));
                }
                
                prevVirtualNode = virtualNodeIdx;
            }
        }

        long[] cost_dist = new long[virtualNodeIdx + 1];
        int[] time_dist = new int[virtualNodeIdx + 1];
        Arrays.fill(cost_dist, COST_INF);
        Arrays.fill(time_dist, TIME_INF);

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(A, 0, 0));
        cost_dist[A] = 0;
        time_dist[A] = 0;

        while (!pq.isEmpty()) {
            Node now = pq.poll();

            if (cost_dist[now.to] < now.cost) continue;
            if (cost_dist[now.to] == now.cost && time_dist[now.to] < now.time) continue;

            for (Node next : graph.get(now.to)) {
                long newCost = now.cost + next.cost;
                int newTime = now.time + next.time;

                if (newCost < cost_dist[next.to]) {
                    cost_dist[next.to] = newCost;
                    time_dist[next.to] = newTime;
                    pq.add(new Node(next.to, newCost, newTime));
                } else if (newCost == cost_dist[next.to] && newTime < time_dist[next.to]) {
                    time_dist[next.to] = newTime;
                    pq.add(new Node(next.to, newCost, newTime));
                }
            }
        }

        long ansCost = cost_dist[B] == COST_INF ? -1 : cost_dist[B];
        long ansTime = time_dist[B] == TIME_INF ? -1 : time_dist[B];

        System.out.println(ansCost + " " + ansTime);
    }
}