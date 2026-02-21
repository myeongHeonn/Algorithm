import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;


class Node implements Comparable<Node> {
    int to, cost, cnt;

    Node(int to, int cost, int cnt) {
        this.to = to;
        this.cost = cost;
        this.cnt = cnt;
    }

    @Override
    public int compareTo(Node o) {
        return this.cost - o.cost;
    }
}

public class Main {

    static int V, E, K;
    static ArrayList<Node>[] graph;
    static int[][] dist;
    static final int INF = Integer.MAX_VALUE;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        st = new StringTokenizer(br.readLine());
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        graph = new ArrayList[V + 1];
        for (int i = 1; i <= V; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            graph[a].add(new Node(b, w, 0));
            graph[b].add(new Node(a, w, 0));
        }

        dist = new int[V + 1][V];
        for (int i = 1; i <= V; i++) {
            Arrays.fill(dist[i], INF);
        }

        dijkstra(start);

        // 세금 0일 때
        int min = INF;
        for (int i = 1; i < V; i++) {
            if (dist[end][i] != INF) {
                min = Math.min(min, dist[end][i]);
            }
        }
        sb.append(min).append("\n");

        int taxSum = 0;

        for (int i = 0; i < K; i++) {
            int tax = Integer.parseInt(br.readLine());
            taxSum += tax;

            min = INF;
            for (int j = 1; j < V; j++) {
                if (dist[end][j] != INF) {
                    min = Math.min(min, dist[end][j] + j * taxSum);
                }
            }
            sb.append(min).append("\n");
        }

        System.out.print(sb);
    }

    static void dijkstra(int start) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(start, 0, 0));
        dist[start][0] = 0;

        while (!pq.isEmpty()) {
            Node cur = pq.poll();

            if (cur.cost > dist[cur.to][cur.cnt]) continue;

            for (Node next : graph[cur.to]) {

                int nextCnt = cur.cnt + 1;
                if (nextCnt >= V) continue;

                int newCost = cur.cost + next.cost;

                boolean flag = false;
                for (int i = 0; i <= nextCnt; i++) {
                    if (dist[next.to][i] <= newCost) {
                        flag = true;
                        break;
                    }
                }
                if (flag) continue;

                if (dist[next.to][nextCnt] > newCost) {
                    dist[next.to][nextCnt] = newCost;
                    pq.offer(new Node(next.to, newCost, nextCnt));
                }
            }
        }
    }
}