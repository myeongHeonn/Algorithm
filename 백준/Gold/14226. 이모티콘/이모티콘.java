import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Scanner;

class Node {
	int screen;
	int clipboard;
	int time;

	public Node(int screen, int clipboard, int time) {
		this.screen = screen;
		this.clipboard = clipboard;
		this.time = time;
	}
}

public class Main {
	// 방문 여부
	static boolean[][] visited = new boolean[1001][1001];

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int s = sc.nextInt();

		Queue<Node> q = new ArrayDeque<>();

		visited[1][0] = true;
		visited[0][0] = true;

		q.add(new Node(1, 0, 0));

		while (!q.isEmpty()) {
			Node cur = q.poll();
			int c_screen = cur.screen;
			int c_clipboard = cur.clipboard;
			int c_time = cur.time;

			if (c_screen == s) {
				System.out.println(c_time);
				break;
			}

			// 복사
			if (!visited[c_screen][c_screen]) {
				q.add(new Node(c_screen, c_screen, c_time + 1));
				visited[c_screen][c_screen] = true;
			}
			// 붙여넣기
			if (c_clipboard != 0 && c_screen + c_clipboard <= 1000) {
				if (!visited[c_screen + c_clipboard][c_clipboard]) {
					q.add(new Node(c_screen + c_clipboard, c_clipboard, c_time + 1));
					visited[c_screen + c_clipboard][c_clipboard] = true;
				}

			}
			// 삭제
			if (c_screen - 1 >= 0) {
				if (!visited[c_screen - 1][c_clipboard]) {
					q.add(new Node(c_screen - 1, c_clipboard, c_time + 1));
					visited[c_screen - 1][c_clipboard] = true;
				}

			}

		}

	}

}
