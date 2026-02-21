import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Stack;
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
	static int[] parents;
	static final int INF = Integer.MAX_VALUE;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int n = Integer.parseInt(br.readLine());
		int m = Integer.parseInt(br.readLine());
		
		graph = new ArrayList[n + 1];
		
		for (int i = 1; i <= n; i++) {
			graph[i] = new ArrayList<>();
		}
		
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());
			
			graph[a].add(new Node(b, w));
		}
		
		st = new StringTokenizer(br.readLine());
		int s = Integer.parseInt(st.nextToken());
		int d = Integer.parseInt(st.nextToken());
		
		dist = new int[n + 1];
		Arrays.fill(dist, INF);
		
		parents = new int[n + 1];
		Arrays.fill(parents, -1);
		
		dijkstra(s, d);
		
		Stack<Integer> stack = new Stack<>();
		stack.add(d);
		
		int count = 2;
		int city = parents[d];
		stack.add(city);
		
		while (true) {
			city = parents[city];
			
			if (city == 0) break;
			
			count++;
			stack.add(city);
		}
		
		sb.append(dist[d]).append("\n");
		sb.append(count).append("\n");
		
		while (!stack.isEmpty()) {
			sb.append(stack.pop() + " ");
		}
		
		System.out.println(sb);
	}
	
	static void dijkstra(int start, int end) {
		PriorityQueue<Node> pq = new PriorityQueue<>();
		
		parents[start] = 0;
		dist[start] = 0;
		pq.offer(new Node(start, 0));
		
		while (!pq.isEmpty()) {
			Node cur = pq.poll();
			
			if (cur.to == end) break;
			
			for (Node next : graph[cur.to]) {
				int newCost = dist[cur.to] + next.cost;
				
				if (dist[next.to] > newCost) {
					parents[next.to] = cur.to;
					dist[next.to] = newCost;
					pq.offer(new Node(next.to, newCost));
				}
			}
		}
	}
}