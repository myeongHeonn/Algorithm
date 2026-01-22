import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Node {
	int value;
	int time;

	Node(int value, int time) {
		this.value = value;
		this.time = time;
	}
}

public class Main {
	// 방문 여부 체크
	static boolean[] visited = new boolean[100001];

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int k = sc.nextInt();

		Queue<Node> q = new LinkedList<>();
		visited[n] = true;
		q.offer(new Node(n, 0));

		while (!q.isEmpty()) {
			Node cur = q.poll();
			int cx = cur.value;
			int time = cur.time;

			if (cx == k) {
				System.out.println(time);
				break;
			}

			int nx_1, nx_2, nx_3;

			nx_3 = 2 * cx;
			if (nx_3 >= 0 && nx_3 < 100001 && !visited[nx_3]) {
				visited[nx_3] = true;
				q.offer(new Node(nx_3, time));
			}

			nx_1 = cx - 1;
			if (nx_1 >= 0 && nx_1 < 100001 && !visited[nx_1]) {
				visited[nx_1] = true;
				q.offer(new Node(nx_1, time + 1));
			}

			nx_2 = cx + 1;
			if (nx_2 >= 0 && nx_2 < 100001 && !visited[nx_2]) {
				visited[nx_2] = true;
				q.offer(new Node(nx_2, time + 1));
			}

		}

	}

}
