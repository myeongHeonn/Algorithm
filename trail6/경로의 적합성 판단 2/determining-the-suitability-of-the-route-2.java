import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    
    static int[] uf;
    
    static int find(int x) {
        if (uf[x] == x) return x;
        
        uf[x] = find(uf[x]);
        return uf[x];
    }
    
    static void union(int x, int y) {
        int X = find(x);
        int Y = find(y);
        
        uf[X] = Y;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        
        uf = new int[n + 1];
        
        for (int i = 1; i <= n; i++) {
            uf[i] = i;
        }
        
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            
            union(a, b);
        }
        
        st = new StringTokenizer(br.readLine());
        
        int now = Integer.parseInt(st.nextToken());
        
        int flag = 1;
        
        for (int i = 1; i < k; i++) {
            
            int next = Integer.parseInt(st.nextToken());
            
            if (find(now) != find(next)) {
                flag = 0;
                break;
            }
            
            now = next;
        }
        
        System.out.println(flag);
    }
}
