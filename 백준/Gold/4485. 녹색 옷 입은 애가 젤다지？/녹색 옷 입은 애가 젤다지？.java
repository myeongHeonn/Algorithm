import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

	static int[] dy = { -1, 1, 0, 0 };
	static int[] dx = { 0, 0, -1, 1 };

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();

		int test_case = 1;

		while (true) {
			int n = Integer.parseInt(br.readLine());
			if (n == 0)
				break;

			int[][] cave = new int[n][n];

			for (int i = 0; i < n; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < n; j++) {
					cave[i][j] = Integer.parseInt(st.nextToken());
				}
			}

			int[][] dist = new int[n][n];
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					dist[i][j] = Integer.MAX_VALUE;
				}
			}

			dist[0][0] = cave[0][0];

			PriorityQueue<int[]> q = new PriorityQueue<>((q1, q2) -> q1[2] - q2[2]);
			q.offer(new int[] { 0, 0, cave[0][0] });

			while (!q.isEmpty()) {
				int[] cur = q.poll();
				int y = cur[0];
				int x = cur[1];

				if (y == n - 1 && x == n - 1) {
					sb.append("Problem " + test_case + ": " + dist[y][x]).append("\n");
					break;
				}

				for (int d = 0; d < 4; d++) {
					int ny = y + dy[d];
					int nx = x + dx[d];

					if (ny < 0 || ny >= n || nx < 0 || nx >= n) continue;

					if (dist[ny][nx] > dist[y][x] + cave[ny][nx]) {
						dist[ny][nx] = dist[y][x] + cave[ny][nx];
						q.offer(new int[] { ny, nx, dist[ny][nx] });
					}
				}
			}

			test_case++;
		}

		System.out.println(sb);
	}
}