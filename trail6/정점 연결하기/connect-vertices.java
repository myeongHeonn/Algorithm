import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    
    static int[] uf;
    
    static void union(int x, int y) {
        int X = find(x);
        int Y = find(y);
        
        if (X != Y) {
            uf[X] = Y;
        }
    }
    
    static int find(int x) {
        if (uf[x] == x) return x;
        
        uf[x] = find(uf[x]);
        return uf[x];
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        int N = Integer.parseInt(br.readLine());
        
        uf = new int[N + 1];
        
        for (int i = 1; i <= N; i++) {
            uf[i] = i;
        }
        
        for (int i = 0; i < N - 2; i++) {
            st = new StringTokenizer(br.readLine());
            
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            
            union(a, b);
        }
        
        int root1 = find(1);
        
        for (int i = 2; i <= N; i++) {
            int root2 = find(i);
            
            if (root1 != root2) {
                System.out.println(1 + " " + i);
                break;
            }
        }
    }
}
