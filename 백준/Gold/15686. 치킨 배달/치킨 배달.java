import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		int n_home = 0;
		int n_chicken = 0;
		
		int[][] city = new int[n][n];
		
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				int value = Integer.parseInt(st.nextToken());
				
				city[i][j] = value;
				
				if (value == 1) n_home++;
				if (value == 2) n_chicken++;
			}
		}
		
		int[][] home = new int[n_home][2];
		int idx_home = 0;
		
		int[][] chicken = new int[n_chicken][2];
		int idx_chicken = 0;
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (city[i][j] == 1) {
					home[idx_home][0] = i;
					home[idx_home++][1] = j;
				}
				
				if (city[i][j] == 2) {
					chicken[idx_chicken][0] = i;
					chicken[idx_chicken++][1] = j;
				}
			}
		}
		
		int answer = Integer.MAX_VALUE;
		
		for (int mask = 0; mask < (1 << n_chicken); mask++) {
			if (Integer.bitCount(mask) != m) continue;
			
			boolean[] selected = new boolean[n_chicken];
			
			for (int i = 0; i < n_chicken; i++) {
				if ((mask & (1 << i)) != 0) {
					selected[i] = true;
				}
			}
			
			int total_dist = 0;
			
			for (int[] h : home) {
				int hy = h[0];
				int hx = h[1];
				
				int dist = Integer.MAX_VALUE;
				
				for (int j = 0; j < n_chicken; j++) {
					if (!selected[j]) continue;
					
					int cy = chicken[j][0];
					int cx = chicken[j][1];
					
					dist = Math.min(dist, Math.abs(hy - cy) + Math.abs(hx - cx));
				}
				
				total_dist += dist;
			}
			
			answer = Math.min(answer, total_dist);
		}
		
		System.out.println(answer);
	}
}