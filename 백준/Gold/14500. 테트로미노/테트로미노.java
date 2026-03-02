import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static int n;
	static int m;
	static int[][] board;
	static int[] dy = { -1, 1, 0, 0 };
	static int[] dx = { 0, 0, -1, 1 };
	static int answer = 0;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		board = new int[n][m];
		
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				dfs(-1, -1, i, j, 1, board[i][j]);
			}
		}
		
		System.out.println(answer);
	}
	
	static void dfs(int py, int px, int y, int x, int depth, int total) {
		if (depth == 4) {
			answer = Math.max(answer, total);
			return;
		}
		
		for (int d = 0; d < 4; d++) {
			int ny = y + dy[d];
			int nx = x + dx[d];
			
			if (ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
			if (ny == py && nx == px) continue;
			
			if (depth == 1) {
				if (d == 0 || d == 1) {
					int ty1 = ny;
					int tx1 = nx - 1;
					int ty2 = ny;
					int tx2 = nx + 1;
					
					if (tx1 >= 0 && tx2 < m) {
						answer = Math.max(answer, total + board[ny][nx] + board[ty1][tx1] + board[ty2][tx2]);
					}
				} else {
					int ty1 = ny - 1;
					int tx1 = nx;
					int ty2 = ny + 1;
					int tx2 = nx;
					
					if (ty1 >= 0 && ty2 < n) {
						answer = Math.max(answer, total + board[ny][nx] + board[ty1][tx1] + board[ty2][tx2]);
					}
				}
			}
			
			dfs(y, x, ny, nx, depth + 1, total + board[ny][nx]);
		}
	}
}