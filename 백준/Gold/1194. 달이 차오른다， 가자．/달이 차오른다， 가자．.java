import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

class Node {
	int y;
	int x;
	int mask;
	int distance;

	Node(int y, int x, int mask, int distance) {
		this.y = y;
		this.x = x;
		this.mask = mask;
		this.distance = distance;
	}
}

public class Main {

	static int n, m;
	static char[][] miro;
	static int[] dy = { -1, 1, 0, 0 };
	static int[] dx = { 0, 0, -1, 1 };
	static char[] keys = { 'a', 'b', 'c', 'd', 'e', 'f' };
	static boolean[][][] visited;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());

		miro = new char[n][m];

		int start_y = 0;
		int start_x = 0;

		for (int i = 0; i < n; i++) {
			String line = br.readLine();
			for (int j = 0; j < m; j++) {
				miro[i][j] = line.charAt(j);

				if (line.charAt(j) == '0') {
					start_y = i;
					start_x = j;
					miro[i][j] = '.';
				}
			}
		}

		visited = new boolean[n][m][64];
		
		Queue<Node> q = new ArrayDeque<>();
		q.offer(new Node(start_y, start_x, 0, 0));
		visited[start_y][start_x][0] = true;
		
		int answer = -1;
		
		while (!q.isEmpty()) {
			Node cur = q.poll();
			int cy = cur.y;
			int cx = cur.x;
			int cmask = cur.mask;
			int cdistance = cur.distance;
		
			if (miro[cy][cx] == '1') {
				answer = cdistance;
				break;
			}
			
			for (int d = 0; d < 4; d++) {
				int ny = cy + dy[d];
				int nx = cx + dx[d];
				int nmask = cmask;
				int ndistance = cdistance + 1;
				
				if (ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
				if (miro[ny][nx] == '#') {
					continue;
				}
				else if (miro[ny][nx] == '.' || miro[ny][nx] == '1') {
					if (visited[ny][nx][nmask]) continue;
					
					visited[ny][nx][nmask] = true;
					q.offer(new Node(ny, nx, nmask, ndistance));
				}
				else if (miro[ny][nx] == 'a' ||
						 miro[ny][nx] == 'b' ||
						 miro[ny][nx] == 'c' ||
						 miro[ny][nx] == 'd' ||
						 miro[ny][nx] == 'e' ||
						 miro[ny][nx] == 'f') {
					int index = (miro[ny][nx] - 97);
					nmask |= (1 << index);
					
					if (visited[ny][nx][nmask]) continue;
					
					visited[ny][nx][nmask] = true;
					q.offer(new Node(ny, nx, nmask, ndistance));
				} else if (miro[ny][nx] == 'A' ||
						   miro[ny][nx] == 'B' ||
						   miro[ny][nx] == 'C' ||
						   miro[ny][nx] == 'D' ||
						   miro[ny][nx] == 'E' ||
						   miro[ny][nx] == 'F') {
					if (visited[ny][nx][nmask]) continue;
					
					if (check(miro[ny][nx], nmask)) {
						visited[ny][nx][nmask] = true;
						
						q.offer(new Node(ny, nx, nmask, ndistance));
					}
					
				}
				
			}
		}
		
		System.out.println(answer);
	}

	// 해당 키가 있으면 해당 문을 통과
	static boolean check(char door, int m) {
		boolean[] isKeys = new boolean[6];

		for (int i = 0; i < 6; i++) {
			if ((m & (1 << i)) != 0) {
				isKeys[i] = true;
			}
		}

		if (isKeys[door - 65]) {
			return true;
		}

		return false;
	}

}