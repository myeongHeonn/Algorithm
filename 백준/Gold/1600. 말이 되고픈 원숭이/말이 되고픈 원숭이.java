import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

class Monkey {
	int y, x, jump;
	
	Monkey (int y, int x, int jump) {
		this.y = y;
		this.x = x;
		this.jump = jump;
	}
}

public class Main {
	
	static int[] h_dy = { -2, -1, 1, 2, 2, 1, -1, -2 };
	static int[] h_dx = { 1, 2, 2, 1, -1, -2, -2, -1 };
	static int[] m_dy = { -1, 1, 0, 0 };
	static int[] m_dx = { 0, 0, -1, 1 };

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int k = Integer.parseInt(br.readLine());
		
		st = new StringTokenizer(br.readLine());
		
		int m = Integer.parseInt(st.nextToken());
		int n = Integer.parseInt(st.nextToken());
		
		int[][] map = new int[n][m];
		
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		int[][][] visited = new int[n][m][k + 1];
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				for (int l = 0; l < k + 1; l++) {
					visited[i][j][l] = Integer.MAX_VALUE;					
				}
			}
		}
		
		Queue<Monkey> q = new ArrayDeque<>();
		
		q.offer(new Monkey(0, 0, 0));
		visited[0][0][0] = 0;
		
		int answer = -1;
		
		while (!q.isEmpty()) {
			Monkey cur = q.poll();
			int cy = cur.y;
			int cx = cur.x;
			int jump = cur.jump;
			
			if (cy == n - 1 && cx == m - 1) {
				answer = visited[cy][cx][jump];
				break;
			}
			
			if (jump == k) {
				for (int d = 0; d < 4; d++) {
					int ny = cy + m_dy[d];
					int nx = cx + m_dx[d];
					
					if (ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
					if (map[ny][nx] == 1) continue;
					if (visited[ny][nx][jump] <= visited[cy][cx][jump] + 1) continue;
					
					visited[ny][nx][jump] = visited[cy][cx][jump] + 1;
					q.offer(new Monkey(ny, nx, jump));
				}
			}
			else {
				for (int d = 0; d < 8; d++) {
					int ny = cy + h_dy[d];
					int nx = cx + h_dx[d];
					
					if (ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
					if (map[ny][nx] == 1) continue;
					if (visited[ny][nx][jump + 1] <= visited[cy][cx][jump] + 1) continue;
					
					visited[ny][nx][jump + 1] = visited[cy][cx][jump] + 1;
					q.offer(new Monkey(ny, nx, jump + 1));
				}
				
				for (int d = 0; d < 4; d++) {
					int ny = cy + m_dy[d];
					int nx = cx + m_dx[d];
					
					if (ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
					if (map[ny][nx] == 1) continue;
					if (visited[ny][nx][jump] <= visited[cy][cx][jump] + 1) continue;
					
					visited[ny][nx][jump] = visited[cy][cx][jump] + 1;
					q.offer(new Monkey(ny, nx, jump));
				}
			}
		}
		
		System.out.println(answer);
	}
}