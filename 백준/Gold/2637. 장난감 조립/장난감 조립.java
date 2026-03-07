import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

class Pair {
    int to;
    int cost;
    
    public Pair (int to, int cost) {
        this.to = to;
        this.cost = cost;
    }
}

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        
        ArrayList<Pair>[] edges = new ArrayList[N + 1];
        int[] indegree = new int[N + 1];
        
        for (int i = 1; i <= N; i++) {
            edges[i] = new ArrayList<>();
        }
        
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            
            int X = Integer.parseInt(st.nextToken());
            int Y = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());
            
            edges[Y].add(new Pair(X, K));
            indegree[X]++;
        }
        
        Queue<Pair> q = new ArrayDeque<>();
        int[][] dp = new int[N + 1][N];
        List<Integer> basic = new ArrayList<>();
        
        for (int i = 1; i <= N; i++) {
            if (indegree[i] == 0) {
                q.offer(new Pair(i, 1));
                basic.add(i);
            }
        }
        
        while (!q.isEmpty()) {
            Pair cur = q.poll();
            
            for (Pair next : edges[cur.to]) {
                if (basic.contains(cur.to)) { 
                    dp[next.to][cur.to] += next.cost;
                }
                else {
                	for (int x : basic) {
                		dp[next.to][x] += dp[cur.to][x] * next.cost;
                	}
                }
                
                indegree[next.to]--;
                
                if (indegree[next.to] == 0) {
                    q.offer(next);
                }
            }
        }
        
        for (int x : basic) {
            sb.append(x).append(" ").append(dp[N][x]).append("\n");
        }
        
        System.out.println(sb);
    }
}