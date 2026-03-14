import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Edge implements Comparable<Edge>{
	int to;
	int cost;
	
	public Edge (int to, int cost) {
		this.to = to;
		this.cost = cost;
	}

	@Override
	public int compareTo(Edge o) {
		return this.cost - o.cost;
	}
}

public class Main {
	
	static final int MAX_N = 1000;
	static final int MAX_M = 100000;
	
	static ArrayList<Edge>[] edges = new ArrayList[MAX_N + 1];
	

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		for (int i = 1; i <= N; i++) {
			edges[i] = new ArrayList<>();
		}
		
		PriorityQueue<Edge> pq = new PriorityQueue<>();
		boolean[] visited = new boolean[N + 1];
		
		st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < K; i++) {
			int x = Integer.parseInt(st.nextToken());
			
			pq.offer(new Edge(x, 0));
		}
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			
			edges[a].add(new Edge(b, c));
			edges[b].add(new Edge(a, c));
		}
		
		int mstCost = 0;
		
		while (!pq.isEmpty()) {
			Edge cur = pq.poll();
			int node = cur.to;
			int cost = cur.cost;
			
			if (visited[node]) continue;
			
			visited[node] = true;
			mstCost += cost;
			
			for (Edge e : edges[node]) {
				if (visited[e.to]) continue;
				pq.offer(e);
			}
		}
		
		System.out.println(mstCost);
	}
}