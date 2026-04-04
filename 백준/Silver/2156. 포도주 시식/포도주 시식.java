import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	
    	int n = Integer.parseInt(br.readLine());
    	
    	int[][] dp = new int[n + 1][3];
    	int[] wine = new int[n + 1];
    	
    	for (int i = 1; i <= n; i++) {
    		wine[i] = Integer.parseInt(br.readLine());
    	}
    	
    	dp[1][0] = 0;
    	dp[1][1] = wine[1];
    	dp[1][2] = wine[1];
    	
    	if (n == 1) {
    		System.out.println(wine[1]);
    	}
    	else {
    		dp[2][0] = Math.max(dp[1][1], dp[1][2]);
    		dp[2][1] = dp[1][0] + wine[2];
    		dp[2][2] = dp[1][1] + wine[2];
    		
    		for (int i = 3; i <= n; i++) {
    			dp[i][0] = Math.max(dp[i - 1][0], Math.max(dp[i - 1][1], dp[i - 1][2]));
    			dp[i][1] = dp[i - 1][0] + wine[i];
    			dp[i][2] = dp[i - 1][1] + wine[i];
    		}
    		
    		int answer = 0;
    		for (int k = 0; k <= 2; k++) {
    			answer = Math.max(answer, dp[n][k]);
    		}
    		
    		System.out.println(answer);
    	}
    }
}