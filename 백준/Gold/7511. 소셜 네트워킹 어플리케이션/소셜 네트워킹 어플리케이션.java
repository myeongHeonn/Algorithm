import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int[] uf;
	
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
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		
		for (int test_case = 1; test_case <= T; test_case++) {
			sb.append("Scenario ").append(test_case).append(":").append("\n");
			
			int n = Integer.parseInt(br.readLine());
			
			uf = new int[n];
			
			for (int i = 0; i < n; i++) {
				uf[i] = i;
			}
			
			int k = Integer.parseInt(br.readLine());
			
			for (int i = 0; i < k; i++) {
				st = new StringTokenizer(br.readLine());
				
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				
				union(a, b);
			}
			
			int m = Integer.parseInt(br.readLine());
			
			for (int i = 0; i < m; i++) {
				st = new StringTokenizer(br.readLine());
				
				int u = Integer.parseInt(st.nextToken());
				int v = Integer.parseInt(st.nextToken());
				
				if (find(u) == find(v)) {
					sb.append(1).append("\n");
				} else {
					sb.append(0).append("\n");
				}
			}
			
			sb.append("\n");
		}
		
		System.out.println(sb);
	}
}
