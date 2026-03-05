import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	
	static int n;
	static ArrayList<Integer>[] tree;
	static boolean[] visited;
	static int[] p;
	static int[][] dp;
	
	static void dfs(int node) {
		
		dp[node][0] = 0;
		dp[node][1] = p[node];
		
		for (int next : tree[node]) {
			if (visited[next]) continue;
			
			visited[next] = true;
			dfs(next);

			dp[node][0] += Math.max(dp[next][0], dp[next][1]);
			dp[node][1] += dp[next][0];
		}
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		n = Integer.parseInt(br.readLine());
		
		tree = new ArrayList[n + 1];
		
		for (int i = 1; i <= n; i++) {
			tree[i] = new ArrayList<>();
		}
		
		p = new int[n + 1];
		
		st = new StringTokenizer(br.readLine());
		for (int i = 1; i <= n; i++) {
			p[i] = Integer.parseInt(st.nextToken());
		}
		
		for (int i = 1; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			tree[a].add(b);
			tree[b].add(a);
		}
		
		visited = new boolean[n + 1];
		dp = new int[n + 1][2];
		visited[1] = true;
		
		dfs(1);
		
		System.out.println(Math.max(dp[1][0], dp[1][1]));
	}
}