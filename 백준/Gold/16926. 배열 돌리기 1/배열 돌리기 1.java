import java.util.Scanner;

public class Main {

	static void rotate(int[][] arr, int line) {
		int N = arr.length;
		int M = arr[0].length;

		int[] dy = { 1, 0, -1, 0 };
		int[] dx = { 0, 1, 0, -1 };

		int y = line;
		int x = line;
		int d = 0;

		int prev = arr[y][x];

		do {
			int ny = y + dy[d];
			int nx = x + dx[d];

			if (ny < line || ny >= N - line || nx < line || nx >= M - line) {
				d++;
				continue;
			}

			int temp = arr[ny][nx];
			arr[ny][nx] = prev;
			prev = temp;

			y = ny;
			x = nx;

		} while (!(y == line && x == line));
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int R = sc.nextInt();

		int[][] arr = new int[n][m];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				arr[i][j] = sc.nextInt();
			}
		}

		for (int r = 0; r < R; r++) {
			for (int k = 0; k < Math.min(n, m) / 2; k++) {
				rotate(arr, k);
			}
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				System.out.print(arr[i][j] + " ");
			}
			System.out.println("");
		}

	}
}