import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	
	static int[] dy = { -1, 0, 0, 1 };
	static int[] dx = { 0, -1, 1, 0 };

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int n = Integer.parseInt(br.readLine());
		
		int[][] space = new int[n][n];

		int sy = 0;
		int sx = 0;

		int m = 0;
		
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				space[i][j] = Integer.parseInt(st.nextToken());
				
				if (space[i][j] == 9) {
					sy = i;
					sx = j;
					space[i][j] = 0;
				}
				
				if (space[i][j] != 0) {
					m++;
				}
			}
		}
        
		int size = 2;
		
		int eatCnt = 0;
		
		int time = 0;
		
		while (true) {
			if (m == 0) break;
			
			PriorityQueue<int[]> q = new PriorityQueue<>((q1, q2) -> {
				if (q1[2] == q2[2]) {
					if (q1[0] == q2[0]) return q1[1] - q2[1];
					return q1[0] - q2[0];					
				}
				
				return q1[2] - q2[2];
			});
			boolean[][] visited = new boolean[n][n];
			
			q.offer(new int[] { sy, sx, 0 });
			visited[sy][sx] = true;
			
			boolean flag = false;
			
			while (!q.isEmpty()) {
				int[] cur = q.poll();
				int cy = cur[0];
				int cx = cur[1];
				int dist = cur[2];
				
				if (space[cy][cx] != 0 && space[cy][cx] < size) {
					m--;
					eatCnt++;
					space[cy][cx] = 0;
					time += dist;
					sy = cy;
					sx = cx;
					flag = true;
					break;
				}
				
				for (int d = 0; d < 4; d++) {
					int ny = cy + dy[d];
					int nx = cx + dx[d];
					
					if (ny < 0 || ny >= n || nx < 0 || nx >= n) continue;
					if (visited[ny][nx]) continue;
					if (space[ny][nx] > size) continue;
					
					visited[ny][nx] = true;
					q.offer(new int[] { ny, nx, dist + 1 });
				}
			}

			if (!flag) break;

			if (eatCnt == size) {
				size++;
				eatCnt = 0;
			}
		}
		
		System.out.println(time);
	}
}