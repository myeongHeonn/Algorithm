import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    
    static int N;
    static int[] uf;
    
    static void union(int x, int y) {
        int X = find(x);
        int Y = find(y);
        
        uf[X] = Y;
    }
    
    static int find(int x) {
        if (uf[x] == x) return x;
        
        uf[x] = find(uf[x]);
        return uf[x];
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        
        uf = new int[N + 1];
        for (int i = 1; i <= N; i++) uf[i] = i;
        
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            
            int command = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            
            if (command == 0) union(x, y);
            else {
                if (find(x) == find(y)) System.out.println(1);
                else System.out.println(0);
            }
        }
    }
}