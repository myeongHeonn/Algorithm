import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    
    public static int[] uf;
    public static int[] sz;
    
    public static void union(int x, int y) {
        int X = find(x);
        int Y = find(y);
        
        if (X != Y) {
            uf[X] = Y;
            sz[Y] += sz[X];
        }
    }
    
    public static int find(int x) {
        if (uf[x] == x) return x;
        
        uf[x] = find(uf[x]);
        return uf[x];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        uf = new int[N + 1];
        sz = new int[N + 1];
        
        for (int i = 1; i <= N; i++) {
            uf[i] = i;
            sz[i] = 1;
        }
        
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            
            union(a, b);
        }
        
        st = new StringTokenizer(br.readLine());
        
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        
        int rootA = find(A);
        int rootB = find(B);
        
        boolean[] checked = new boolean[N + 1];
        checked[rootA] = true;
        
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>((a, b) -> b.compareTo(a));
        
        for (int i = 1; i <= N; i++) {
            int root = find(i);
            
            if (root == rootB || root == rootA) continue;
            if (checked[root]) continue;
            
            pq.add(sz[root]);
            checked[root] = true;
        }

        int ans = sz[rootA];
        
        int cnt = 0;
        
        while(cnt < K) {
            if (pq.isEmpty()) break;
            
            ans += pq.poll();
            cnt++;
        }
        
        System.out.println(ans);
    }
}