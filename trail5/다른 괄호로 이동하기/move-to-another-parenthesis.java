import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    
    static int INF = 1_000_000_000;
    
    static int[] dy = { -1, 1, 0, 0 };
    static int[] dx = { 0, 0, -1, 1 };
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        
        char[][] grid = new char[N][N];
        
        
        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            
            for (int j = 0; j < N; j++) {
                char c = s.charAt(j);
                grid[i][j] = c;
            }
        }
        
        int max = 0;
        
        for (int sy = 0; sy < N; sy++) {
            for (int sx = 0; sx < N; sx++) {
                
                int[][] dist = new int[N][N];
                
                for (int i = 0; i < N; i++) {
                    for (int j = 0; j < N; j++) {
                        dist[i][j] = INF;
                    }
                }
                
                Queue<int[]> q = new ArrayDeque<int[]>();
                q.add(new int[] { sy, sx, 0 });
                dist[sy][sx] = 0;
                
                while(!q.isEmpty()) {
                    int[] now = q.poll();
                    int cy = now[0];
                    int cx = now[1];
                    int c_cost = now[2];
                    
                    for (int i = 0; i < 4; i++) {
                        int ny = cy + dy[i];
                        int nx = cx + dx[i];
                        
                        if (ny < 0 || ny >= N || nx < 0 || nx >= N) continue;
                        
                        int n_cost = c_cost + ((grid[cy][cx] == grid[ny][nx]) ? A : B);
                        
                        if (n_cost < dist[ny][nx]) {
                            dist[ny][nx] = n_cost;
                            q.add(new int[] { ny, nx, n_cost});
                        }
                    }
                }
                
                for (int i = 0; i < N; i++) {
                    for (int j = 0; j < N; j++) {
                        max = Math.max(max, dist[i][j]);
                    }
                }
            }
        }
        
        System.out.println(max);
    }
}