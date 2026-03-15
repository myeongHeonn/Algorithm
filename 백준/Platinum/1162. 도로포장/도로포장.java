import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Edge implements Comparable<Edge> {
	int to;
	long cost;
	int cnt;
	
	public Edge (int to, long cost, int cnt) {
		this.to = to;
		this.cost = cost;
		this.cnt = cnt;
	}

	@Override
	public int compareTo(Edge o) {
		return Long.compare(this.cost, o.cost);
	}
}

public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		ArrayList<Edge>[] graph = new ArrayList[N + 1];
		
		for (int i = 1; i <= N; i++) {
			graph[i] = new ArrayList<>();
		}
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			long c = (long) Integer.parseInt(st.nextToken());
			
			graph[a].add(new Edge(b, c, 0));
			graph[b].add(new Edge(a, c, 0));
		}
		
		long[][] dist = new long[N + 1][K + 1];
		
		for (int i = 1; i <= N; i++) {
			Arrays.fill(dist[i], Long.MAX_VALUE);
		}
		
		PriorityQueue<Edge> pq = new PriorityQueue<>();
		
		pq.offer(new Edge(1, 0, 0));
		dist[1][0] = 0;
		
		while (!pq.isEmpty()) {
			Edge cur = pq.poll();
			int node = cur.to;
			long totalCost = cur.cost;
			int cnt = cur.cnt;
			
			if (dist[node][cnt] < totalCost) continue;
			
			for (Edge e : graph[node]) {
				int next = e.to;
				long newTotalCost = totalCost + e.cost;
				
				// 포장하지 않는 경우
				if (dist[next][cnt] > newTotalCost) {
					dist[next][cnt] = newTotalCost;
					pq.offer(new Edge(next, newTotalCost, cnt));
				}
				
				// 포장 하는 경우
				if (cnt < K && dist[next][cnt + 1] > totalCost) {
					dist[next][cnt + 1] = totalCost;
					pq.offer(new Edge(next, totalCost, cnt + 1));
				}
			}
		}
		
		long answer = Long.MAX_VALUE;
		
		for (int i = 0; i <= K; i++) {
			answer = Math.min(answer, dist[N][i]);
		}
		
		System.out.println(answer);
	}
}
