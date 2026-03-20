import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Edge {
	int to;
	int cost;
	
	public Edge (int to, int cost) {
		this.to = to;
		this.cost = cost;
	}
}

public class Main {
	
	static final int MAX_N = 200000;
	
	static ArrayList<Edge>[] edges = new ArrayList[MAX_N + 1];
	static int[] distS = new int[MAX_N + 1];
	static int[] distE = new int[MAX_N + 1];
	static int[] distBack = new int[MAX_N + 1];
	static boolean[] visited = new boolean[MAX_N + 1];

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		for (int i = 1; i <= N; i++) {
			edges[i] = new ArrayList<>();
		}
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			
			edges[a].add(new Edge(b, c));
			edges[b].add(new Edge(a, c));
		}
		
		for (int i = 1; i <= N; i++) {
			Collections.sort(edges[i], (a, b) -> a.to - b.to);
		}
		
		st = new StringTokenizer(br.readLine());
		
		int S = Integer.parseInt(st.nextToken());
		int E = Integer.parseInt(st.nextToken());
		
		Arrays.fill(distS, Integer.MAX_VALUE);
		Arrays.fill(distE, Integer.MAX_VALUE);
		
		dijkstra(S, distS);
		dijkstra(E, distE);
		
		int totalCost = distS[E];
		int cur = S;
		
		while (cur != E) {
			for (Edge e : edges[cur]) {
				int next = e.to;
				int cost = e.cost;
				
				if (distS[cur] + cost + distE[next] == totalCost) {
					cur = next;
					visited[cur] = true;
					break;
				}
			}
		}
		
		Arrays.fill(distBack, Integer.MAX_VALUE);
		
		dijkstraBack(E, distBack);
		
		totalCost += distBack[S];
		
		System.out.println(totalCost);
	}
	
	static void dijkstra(int start, int dist[]) {
		PriorityQueue<Edge> pq = new PriorityQueue<>((a, b) -> a.cost - b.cost);
		
		pq.add(new Edge(start, 0));
		dist[start] = 0;
		
		while (!pq.isEmpty()) {
			Edge cur = pq.poll();

			int node = cur.to;
			int cost = cur.cost;
			
			if (dist[node] < cost) continue;
			
			for (Edge e : edges[node]) {
				int next = e.to;
				int newCost = dist[node] + e.cost;
				
				if (dist[next] > newCost) {
					dist[next] = newCost;
					pq.add(new Edge(next, newCost));
				}
			}
		}
	}
	
	static void dijkstraBack(int start, int dist[]) {
		PriorityQueue<Edge> pq = new PriorityQueue<>((a, b) -> a.cost - b.cost);
		
		pq.add(new Edge(start, 0));
		dist[start] = 0;
		
		while (!pq.isEmpty()) {
			Edge cur = pq.poll();

			int node = cur.to;
			int cost = cur.cost;
			
			if (dist[node] < cost) continue;
			
			for (Edge e : edges[node]) {
				int next = e.to;
				int newCost = dist[node] + e.cost;
				
				if (visited[next]) continue;
				
				if (dist[next] > newCost) {
					dist[next] = newCost;
					pq.add(new Edge(next, newCost));
				}
			}
		}
	}
}