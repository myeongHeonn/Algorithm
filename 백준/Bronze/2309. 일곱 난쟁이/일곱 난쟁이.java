import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		// 입력
		int[] arr = new int[9];
		for (int i = 0; i < 9; i++) { arr[i] = sc.nextInt(); }
		
		loop:
		for (int i = 0; i < 9; i++) {
			for (int j = i + 1; j < 9; j++) {
				
				int[] temp = new int[7];
				int sum = 0;
				int index = 0;
				// 2명을 제외하고 7명의 키 합 구하기
				for (int k = 0; k < 9; k++) {
					if (k == i || k == j) {
						continue;
					} else {
						temp[index] = arr[k];
						index++;
						sum += arr[k];
					}
				}
				// 합이 100일 경우 오름차순으로 정렬 후 출
				if (sum == 100) {
					Arrays.sort(temp);
					for (int x : temp) { System.out.println(x); }
					break loop;
				}
			}
		}
	}
}