import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		Queue<Integer> queue = new LinkedList<>();
		for (int i = 1; i < n + 1; i++) {
			queue.offer(i);
		}
		
		int flag = 1;
		while (queue.size() != 1) {
			if (flag == 1) {
				queue.poll();
				flag = 2;
			} else {
				queue.offer(queue.poll());
				flag = 1;
			}
		}
		
		System.out.println(queue.poll());
	}
}