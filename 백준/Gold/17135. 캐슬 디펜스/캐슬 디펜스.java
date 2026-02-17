import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

	static int n;
	static int m;
	static int d;
	static int[][] board;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		d = Integer.parseInt(st.nextToken());

		board = new int[n][m];

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		int answer = 0;
		
		for (int mask = 0; mask < (1 << m); mask++) {
			if (Integer.bitCount(mask) != 3) continue;
			
			int[] archer = new int[3];
			int index = 0;
			
			for (int i = 0; i < m; i++) {
				if ((mask & (1 << i)) != 0) {
					archer[index++] = i;
				}
			}
			
			int kill = 0;
			int[][] temp = new int[n][m];
			for (int i = 0; i < n; i++) {
				temp[i] = board[i].clone();
			}
			
			// n턴 만큼 게임 진행
			for (int i = 0; i < n; i++) {
				
				ArrayList<int[]> enemy = new ArrayList<>();
				
				for (int j = 0; j < 3; j++) {
					int y = n - i;
					int x = archer[j];
					
					int[] attack = remove(y, x, temp);
					if (attack != null) {
						enemy.add(attack);
					}
				}
				
				for (int[] e : enemy) {
					if (temp[e[0]][e[1]] != 0) {
						kill++;
						temp[e[0]][e[1]] = 0;						
					}
				}
			}
			
			answer = Math.max(answer, kill);
		}
		
		System.out.println(answer);
	}

	// 궁수의 위치에서 죽일 수 있는 가장 가까운 적을 반환하는 메서드
	static int[] remove(int y, int x, int[][] temp) {
		
		for (int k = 1; k <= d; k++) {
			for (int j = 0; j < m; j++) {
				for (int i = y - 1; i >= 0; i--) {
					int dist = (y - i) + Math.abs(x - j);
					
					if (dist > k) continue;
					
					if (dist <= k && temp[i][j] == 1) {
						return new int[] { i, j };
					}
				}
			}
		}
		
		return null;
	}

}