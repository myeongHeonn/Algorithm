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
		
		int N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
		
		uf = new int[N + 1];
		
		for (int i = 0; i <= N; i++) {
			uf[i] = i;
		}
		
		int cnt = 0;
		
		for (int i = 0; i < M; i++) {
			int plane = Integer.parseInt(br.readLine());
			
			int gate = find(plane);
			
			if (gate == 0) break;
			
			union(gate, gate - 1);
			cnt++;
		}
		
		System.out.println(cnt);
	}
}
