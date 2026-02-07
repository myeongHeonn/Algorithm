import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int s = Integer.parseInt(st.nextToken());
		
		int[] arr = new int[n];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		int count = 0;
		for (int mask = 1; mask < (1 << n); mask++) {
			int sum = 0;
			
			for (int i = 0; i < n; i++) {
				if ((mask & (1 << i)) != 0) {
					sum += arr[i];
				}
			}
			
			if (sum == s) count++;
		}
		
		System.out.println(count);
		
	}

}