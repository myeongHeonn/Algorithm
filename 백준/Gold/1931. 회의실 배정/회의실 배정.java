import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int n = Integer.parseInt(br.readLine());
		int[][] meeting = new int[n][2];
		
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			meeting[i][0] = Integer.parseInt(st.nextToken());
			meeting[i][1] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(meeting, (a, b) -> {
			if (a[0] == b[0]) return a[1] - b[1];
			return a[0] - b[0];
		});
		
		int prev_start = meeting[0][0];
		int prev_end = meeting[0][1];
		int count = 1;
		
		for (int i = 1; i < n; i++) {
			if (meeting[i][0] >= prev_end) {
				prev_start = meeting[i][0];
				prev_end = meeting[i][1];
				count++;
			}
			
			if (meeting[i][0] == prev_start) continue;
			
			if (meeting[i][1] < prev_end) {
				prev_start = meeting[i][0];
				prev_end = meeting[i][1];
			}
			
		}
		
		System.out.println(count);
	}
}