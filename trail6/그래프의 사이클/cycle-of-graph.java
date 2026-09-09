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
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        
        uf = new int[N + 1];
        for (int i = 1; i <= N; i++) uf[i] = i;
        
        boolean flag = false;
        
        for (int i = 1; i <= M; i++) {
            st = new StringTokenizer(br.readLine());
            
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            
            if (find(a) != find(b)) {
                union(a, b);
            }
            else {
                System.out.println(i);
                flag = true;
                break;
            }
        }
        
        if (!flag) System.out.println("happy");
    }
}
