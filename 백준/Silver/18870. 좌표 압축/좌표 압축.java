import java.io.*;
import java.util.*;

public class Main {

    static int lowerBound(int[] arr, int target) {
        int left = 0;
        int right = arr.length;

        while (left < right) {
            int mid = (left + right) / 2;

            if (arr[mid] >= target) right = mid;
            else left = mid + 1;
        }

        return left;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        int[] sorted = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            sorted[i] = arr[i];
        }

        Arrays.sort(sorted);

        int[] unique = Arrays.stream(sorted).distinct().toArray();

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < N; i++) {
            int idx = lowerBound(unique, arr[i]);
            sb.append(idx).append(" ");
        }

        System.out.println(sb);
    }
}