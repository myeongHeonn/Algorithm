import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int[] uf;
	
	static void union(int a, int b) {
		int root_a = find(a);
		int root_b = find(b);
		
		uf[root_a] = root_b;
	}
	
	static int find(int x) {
		if (uf[x] == x) return x;
		
		int root = find(uf[x]);
		uf[x] = root;
		
		return uf[x];
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		uf = new int[n + 1];
		
		for (int i = 0; i <= n; i++) {
			uf[i] = i;
		}
		
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			
			int command = Integer.parseInt(st.nextToken());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			if (command == 0) {
				union(a, b);
			} else {
				if (find(a) == find(b)) {
					sb.append("YES").append("\n");
				} else {
					sb.append("NO").append("\n");
				}
			}
		}
		
		System.out.println(sb);
	}

}
