import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Node implements Comparable<Node> {
	int to;
	int cost;
	
	Node(int to, int cost) {
		this.to = to;
		this.cost = cost;
	}
	
	@Override
	public int compareTo(Node o) {
		return this.cost - o.cost;
	}
}

public class Solution {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        
        for (int test_case = 1; test_case <= T; test_case++) {
        	st = new StringTokenizer(br.readLine());
        	
            int V = Integer.parseInt(st.nextToken());
            int E = Integer.parseInt(st.nextToken());

        	ArrayList<Node>[] graph = new ArrayList[V + 1];
        	for (int i = 1; i <= V; i++) {
        		graph[i] = new ArrayList<>();
        	}
        	
        	for (int i = 0; i < E; i++) {
                st = new StringTokenizer(br.readLine());
                
                int A = Integer.parseInt(st.nextToken());
                int B = Integer.parseInt(st.nextToken());
                int C = Integer.parseInt(st.nextToken());

                graph[A].add(new Node(B, C));
                graph[B].add(new Node(A, C));
            }
        	
        	boolean[] visited = new boolean[V + 1];
        	PriorityQueue<Node> pq = new PriorityQueue<>();
        	
        	long mstCost = 0;
        	int count = 0;
        	
        	pq.offer(new Node(1, 0));
        	
        	while (!pq.isEmpty()) {
        		Node cur = pq.poll();
        		
        		if (visited[cur.to]) continue;
        		
        		visited[cur.to] = true;
        		mstCost += cur.cost;
        		count++;
        		
        		if (count == V) break;
        		
        		for (Node next : graph[cur.to]) {
        			if (!visited[next.to]) {
        				pq.offer(next);
        			}
        		}
        	}
        	
        	sb.append("#" + test_case + " " + mstCost).append("\n");
        }
        
        System.out.println(sb);
	}
}