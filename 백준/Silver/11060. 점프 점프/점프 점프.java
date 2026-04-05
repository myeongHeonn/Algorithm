import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        int[] dp = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;

        for (int i = 0; i < n; i++) {
            if (dp[i] == Integer.MAX_VALUE) continue;

            for (int j = 1; j <= arr[i]; j++) {
                int next = i + j;

                if (next >= n) break;

                dp[next] = Math.min(dp[next], dp[i] + 1);
            }
        }

        System.out.println(dp[n - 1] == Integer.MAX_VALUE ? -1 : dp[n - 1]);
    }
}