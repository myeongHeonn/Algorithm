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
		
		st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		uf = new int[n];
		
		for (int i = 0; i < n; i++) {
			uf[i] = i;
		}
		
		int order = 0;
		
		for (int i = 1; i <= m; i++) {
			st = new StringTokenizer(br.readLine());
			
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			if (find(a) == find(b)) {
				order = i;
				break;
			} else {
				union(a, b);
			}
		}
		
		System.out.println(order);
	}
}
