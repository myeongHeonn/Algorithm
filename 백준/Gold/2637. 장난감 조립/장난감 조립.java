/**
 * @Problem : BOJ 2637 장난감 조립
 * @Category : 위상 정렬
 * @Time : 104 ms (시간 제한 : 1초)
 * @Memory : 14 MB (메모리 제한 : 128 MB)
 * 
 * @Idea
 * dp[i][j] -> i번 부품을 조립하는데 필요한 기본 부품 j 수
 * 
 * @TimeComplexity : O(M * B)
 * @SpaceComplexity : O(N^2)
 * N <= 100
 * M <= 100
 * B <= N - 1 = 99
 */

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
        boolean[] isBasic = new boolean[N + 1];
        
        for (int i = 1; i <= N; i++) {
            if (indegree[i] == 0) {
                q.offer(new Pair(i, 1));
                isBasic[i] = true;
            }
        }
        
        while (!q.isEmpty()) {
            Pair cur = q.poll();
            
            for (Pair next : edges[cur.to]) {
                if (isBasic[cur.to]) { 
                    dp[next.to][cur.to] += next.cost;
                }
                else {
                	for (int i = 1; i <= N; i++) {
                		if (isBasic[i]) {
                			dp[next.to][i] += dp[cur.to][i] * next.cost;
                		}
                	}
                }
                
                indegree[next.to]--;
                
                if (indegree[next.to] == 0) {
                    q.offer(next);
                }
            }
        }
        
    	for (int i = 1; i <= N; i++) {
    		if (isBasic[i]) {
    			sb.append(i).append(" ").append(dp[N][i]).append("\n");
    		}
    	}
        
        System.out.println(sb);
    }
}