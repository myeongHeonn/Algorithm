import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int N;
	static int[][] S;
	static int answer = Integer.MAX_VALUE;
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		S = new int[N][N];
		
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				S[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		// 모든 부분집합 탐색
		for (int mask = 0; mask < (1 << N); mask++) {
			if (Integer.bitCount(mask) != N / 2) continue;
			
			int start = 0;
			int link = 0;
			
			// 팀 능력치 계산
			for (int i = 0; i < N; i++) {
				for (int j = i + 1; j < N; j++) {
					
					// 둘 다 0 -> 스타트 팀
					if ((mask & (1 << i)) == 0 && (mask & (1 << j)) == 0) {
						start += S[i][j] + S[j][i];
					}
					// 둘 다 1 -> 링크 팀
					else if ((mask & (1 << i)) != 0 && (mask & (1 << j)) != 0) {
						link += S[i][j] + S[j][i];
					}
				}
			}
			
			answer = Math.min(answer, Math.abs(start - link));
		}
		
		System.out.println(answer);
	}

}