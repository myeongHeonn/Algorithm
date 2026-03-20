import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		
		st = new StringTokenizer(br.readLine());
		
		int[] S = new int[N];
		
		boolean[] visited = new boolean[20000001];
		
		for (int i = 0; i < N; i++) {
			S[i] = Integer.parseInt(st.nextToken());
		}
		
		for (int mask = 1; mask < (1 << N); mask++) {
			
			int total = 0;
			
			for (int i = 0; i < N; i++) {
				if ((mask & (1 << i)) != 0) {
					total += S[i];
				}
			}
			
			visited[total] = true;
		}
		
		for (int i = 1; i <= 20000001; i++) {
			if (!visited[i]) {
				System.out.println(i);
				break;
			}
		}
	}

}
