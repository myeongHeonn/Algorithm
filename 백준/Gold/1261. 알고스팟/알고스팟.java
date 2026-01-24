import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

class Node {
	int y;
	int x;
	int aoj;

	public Node(int y, int x, int aoj) {
		this.y = y;
		this.x = x;
		this.aoj = aoj;
	}

}

public class Main {
	// [y][x][0] -> -1 or 1 (방문여부) / [y][x][1] - 벽 부순 횟수
	static int[][][] visited = new int[100][100][2];
	static {
		for (int i = 0; i < 100; i++) {
			for (int j = 0; j < 100; j++) {
				Arrays.fill(visited[i][j], -1);
			}
		}
	}

	// 범위 체크
	static boolean check(int n, int m, int y, int x) {
		if (y >= 0 && y < n && x >= 0 && x < m) {
			return true;
		} else {
			return false;
		}
	}

	// 이동
	static int[] dy = { -1, 1, 0, 0 };
	static int[] dx = { 0, 0, -1, 1 };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int m = Integer.parseInt(st.nextToken());
		int n = Integer.parseInt(st.nextToken());

		int[][] board = new int[n][m];

		for (int i = 0; i < n; i++) {
			String line = br.readLine();
			for (int j = 0; j < m; j++) {
				board[i][j] = line.charAt(j) - '0';
			}
		}

		Queue<Node> q = new ArrayDeque<>();
		q.add(new Node(0, 0, 0));
		visited[0][0][0] = 1;
		visited[0][0][1] = 0;
		visited[n - 1][m - 1][1] = 200;

		while (!q.isEmpty()) {
			Node cur = q.poll();
			int cy = cur.y;
			int cx = cur.x;
			int aoj = cur.aoj;

			if (cy == n - 1 && cx == m - 1) {
				visited[cy][cx][1] = Math.min(visited[cy][cx][1], aoj);
				continue;
			}

			for (int k = 0; k < 4; k++) {
				int ny = cy + dy[k];
				int nx = cx + dx[k];

				if (check(n, m, ny, nx)) {
					// board[ny][nx]에 벽이 없는 경우
					if (board[ny][nx] == 0) {
						// 다음 노드에 첫 방문인 경우
						if (visited[ny][nx][0] == -1) {
							visited[ny][nx][0] = 1;
							visited[ny][nx][1] = aoj;
							q.add(new Node(ny, nx, aoj));
						} // 방문한 적이 있는 경우
						else {
							if (aoj < visited[ny][nx][1]) {
								visited[ny][nx][1] = aoj;
								q.add(new Node(ny, nx, aoj));
							}
						}
						// board[ny][nx]에 벽이 있는 경우
					} else {
						// 다음 노드에 첫 방문인 경우
						if (visited[ny][nx][0] == -1) {
							visited[ny][nx][0] = 1;
							visited[ny][nx][1] = aoj + 1;
							q.add(new Node(ny, nx, aoj + 1));
						} // 방문한 적이 있는 경우
						else {
							if (aoj + 1 < visited[ny][nx][1]) {
								visited[ny][nx][1] = aoj + 1;
								q.add(new Node(ny, nx, aoj + 1));
							}
						}

					}

				}

			}
		}

		System.out.println(visited[n - 1][m - 1][1]);

	}

}
