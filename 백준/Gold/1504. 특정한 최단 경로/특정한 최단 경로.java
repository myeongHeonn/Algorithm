import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Node implements Comparable<Node> {
	int to, cost;
	
	public Node (int to, int cost) {
		this.to = to;
		this.cost = cost;
	}

	@Override
	public int compareTo(Node o) {
		return this.cost - o.cost;
	}
}

public class Main {
	
	static ArrayList<Node>[] graph;
	static int[] dist;
	static final int INF = Integer.MAX_VALUE;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		int V = Integer.parseInt(st.nextToken());
		int E = Integer.parseInt(st.nextToken());
		
		graph = new ArrayList[V + 1];
		
		for (int i  = 1; i <= V; i++) {
			graph[i] = new ArrayList<>();
		}
		
		for (int i = 0; i < E; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			
			graph[a].add(new Node(b, c));
			graph[b].add(new Node(a, c));
		}
		
		st = new StringTokenizer(br.readLine());
		int v1 = Integer.parseInt(st.nextToken());
		int v2 = Integer.parseInt(st.nextToken());
		
		dist = new int[V + 1];
		
		// 1 -> v1 -> v2 -> V
		boolean possible1 = true;
		int sum1 = 0;
		
		Arrays.fill(dist, INF);
		dijkstra(1, v1);
		
		if (dist[v1] == INF) possible1 = false;
		else sum1 += dist[v1];
		
		Arrays.fill(dist, INF);
		dijkstra(v1, v2);
		
		if (dist[v2] == INF) possible1 = false;
		else sum1 += dist[v2];
		
		Arrays.fill(dist, INF);
		dijkstra(v2, V);
		
		if (dist[V] == INF) possible1 = false;
		else sum1 += dist[V];
		
		// 1 -> v2 -> v1 -> V
		boolean possible2 = true;
		int sum2 = 0;
		
		Arrays.fill(dist, INF);
		dijkstra(1, v2);
		
		if (dist[v2] == INF) possible2 = false;
		else sum2 += dist[v2];
		
		Arrays.fill(dist, INF);
		dijkstra(v2, v1);
		
		if (dist[v1] == INF) possible2 = false;
		else sum2 += dist[v1];
		
		Arrays.fill(dist, INF);
		dijkstra(v1, V);
		
		if (dist[V] == INF) possible2 = false;
		else sum2 += dist[V];
		
		
		if (!possible1 && !possible2) System.out.println(-1);
		else if (possible1 && !possible2) System.out.println(sum1);
		else if (!possible1 && possible2) System.out.println(sum2);
		else if (possible1 && possible2) System.out.println(Math.min(sum1, sum2));
	}
	
	static void dijkstra(int start, int end) {
		PriorityQueue<Node> pq = new PriorityQueue<>();
		
		dist[start] = 0;
		pq.offer(new Node(start, 0));
		
		while (!pq.isEmpty()) {
			Node cur = pq.poll();
			
			if (cur.to == end) break;
			
			for (Node next : graph[cur.to]) {
				int newCost = dist[cur.to] + next.cost;
				
				if (dist[next.to] > newCost) {
					dist[next.to] = newCost;
					pq.offer(new Node(next.to, newCost));
				}
			}
		}
	}
}