import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    
    public static int[] uf;
    
    public static boolean union(int x, int y) {
        int X = find(x);
        int Y = find(y);
        
        if (X == Y) {
            return true;
        }
        else {
            uf[X] = Y;
            return false;
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
        for (int i = 1; i <= N; i++) {
            uf[i] = i;
        }
        
        int cnt = 0;
        
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            
            if (union(a, b)) cnt++;
        }
        
        for (int i = 2; i <= N; i++) {
            if (find(1) != find(i)) {
                cnt++;
                union(1, i);
            }
        }
        
        System.out.println(cnt);
    }
}