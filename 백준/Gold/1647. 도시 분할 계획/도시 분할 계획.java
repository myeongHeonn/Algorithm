import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

class Tuple implements Comparable<Tuple> {
	int x;
	int y;
	int cost;
	
	public Tuple (int x, int y, int cost) {
		this.x = x;
		this.y = y;
		this.cost = cost;
	}

	@Override
	public int compareTo(Tuple o) {
		return this.cost - o.cost;
	}
}

public class Main {
	
	static final int MAX_N = 100_000;
	
	static int[] uf = new int[MAX_N + 1];
	
	static void union(int x, int y) {
		int X = find(x);
		int Y = find(y);
		
		uf[X] = Y;
	}
	
	static int find(int x) {
		if (uf[x] == x) return x;
		return uf[x] = find(uf[x]);
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		for (int i = 1; i <= N; i++) {
			uf[i] = i;
		}
		
		Tuple[] edges = new Tuple[M];
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			
			edges[i] = new Tuple(a, b, c);
		}
		
		Arrays.sort(edges);
		
		int maxCost = 0;
		int mstCost = 0;
		
		for (int i = 0; i < M; i++) {
			int x = edges[i].x;
			int y = edges[i].y;
			int cost = edges[i].cost;
			
			if (find(x) != find(y)) {
				mstCost += cost;
				maxCost = Math.max(maxCost, cost);
				
				union(x, y);
			}
		}
		
		System.out.println(mstCost - maxCost);
	}
}