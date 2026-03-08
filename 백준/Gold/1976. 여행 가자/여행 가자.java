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
		
		int n = Integer.parseInt(br.readLine());
		
		uf = new int[n + 1];
		
		for (int i = 1; i <= n; i++) {
			uf[i] = i;
		}
		
		int m = Integer.parseInt(br.readLine());
		
		for (int i = 1; i <= n; i++) {
			st = new StringTokenizer(br.readLine());
			
			for (int j = 1; j <= n; j++) {
				int info = Integer.parseInt(st.nextToken());
				
				if (info == 1) {
					union(i, j);
				}
			}
		}
		
		st = new StringTokenizer(br.readLine());
		
		int root = find(Integer.parseInt(st.nextToken()));
		
		boolean connect = true;
		
		for (int i = 0; i < m - 1; i++) {
			int city = Integer.parseInt(st.nextToken());
			
			if (root != find(city)) {
				connect = false;
				break;
			}
		}
		
		if (connect) {
			System.out.println("YES");
		} else {
			System.out.println("NO");
		}
	}
}
