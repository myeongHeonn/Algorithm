import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.TreeMap;

class Jewel {
    int weight;
    int value;

    Jewel(int weight, int value) {
        this.weight = weight;
        this.value = value;
    }
}

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        Jewel[] jewels = new Jewel[N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            jewels[i] = new Jewel(
                Integer.parseInt(st.nextToken()),
                Integer.parseInt(st.nextToken())
            );
        }

        Arrays.sort(jewels, (a, b) -> b.value - a.value);

        TreeMap<Integer, Integer> bags = new TreeMap<>();

        for (int i = 0; i < K; i++) {
            int size = Integer.parseInt(br.readLine());
            bags.put(size, bags.getOrDefault(size, 0) + 1);
        }

        long answer = 0;

        for (Jewel j : jewels) {

            Integer bag = bags.ceilingKey(j.weight);

            if (bag != null) {

                answer += j.value;

                if (bags.get(bag) == 1) {
                    bags.remove(bag);
                } else {
                    bags.put(bag, bags.get(bag) - 1);
                }
            }
        }

        System.out.println(answer);
    }
}