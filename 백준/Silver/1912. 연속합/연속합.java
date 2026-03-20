import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int n = Integer.parseInt(br.readLine());
		
		st = new StringTokenizer(br.readLine());
		
		int[] S = new int[n];
		
		for (int i = 0; i < n; i++) {
			S[i] = Integer.parseInt(st.nextToken());
		}
		
		int[] dp = new int[n];
		dp[0] = S[0];
		
		for (int i = 1; i < n; i++) {
			dp[i] = Math.max(S[i], dp[i - 1] + S[i]);
		}
		
		int answer = dp[0];
		
		for (int i = 1; i < n; i++) {
			answer = Math.max(answer, dp[i]);
		}
		
		System.out.println(answer);
	}
}
