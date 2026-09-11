import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static int INF = 1_000_000_000;
    
    public static int N;
    
    public static int[][] graph;
    public static boolean[] visited;
    
    public static int[] dist;
    public static int[] path;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        
        graph = new int[N + 1][N + 1];
        visited = new boolean[N + 1];
        dist = new int[N + 1];
        path = new int[N + 1];
        
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            
            graph[a][b] = c;
            graph[b][a] = c;
        }
        
        for (int i = 1; i <= N; i++) {
            dist[i] = INF;
        }
        
        dijkstra_path();
        
        int origin_min = dist[N];
        
        int node = N;
        
        int max = -1;
        
        while(node != 1) {
            int prev = path[node];
            
            int origin_cost = graph[prev][node];
            
            graph[prev][node] = 2 * origin_cost;
            graph[node][prev] = 2 * origin_cost;
            
            for (int i = 1; i <= N; i++) {
                visited[i] = false;
                dist[i] = INF;
            }
            
            dijkstra();
            
            max = Math.max(max, dist[N]);
            
            graph[prev][node] = origin_cost;
            graph[node][prev] = origin_cost;
            
            node = prev;
        }
        
        System.out.println(max - origin_min);
    }
    
    public static void dijkstra_path() {
        dist[1] = 0;
        path[1] = -1;
        
        for (int i = 1; i <= N; i++) {
            int minIndex = -1;
            
            for (int j = 1; j <= N; j++) {
                if (visited[j]) continue;
                
                if (minIndex == -1 || dist[minIndex] > dist[j]) {
                    minIndex = j;
                }
            }
            
            visited[minIndex] = true;
            
            for (int j = 1; j <= N; j++) {
                if (graph[minIndex][j] == 0) continue;
                
                if (dist[j] > dist[minIndex] + graph[minIndex][j]) {
                    dist[j] = dist[minIndex] + graph[minIndex][j];
                    path[j] = minIndex;
                }
            }
        }
    }
    
    public static void dijkstra() {
        dist[1] = 0;
        
        for (int i = 1; i <= N; i++) {
            int minIndex = -1;
            
            for (int j = 1; j <= N; j++) {
                if (visited[j]) continue;
                
                if (minIndex == -1 || dist[minIndex] > dist[j]) {
                    minIndex = j;
                }
            }
            
            visited[minIndex] = true;
            
            for (int j = 1; j <= N; j++) {
                if (graph[minIndex][j] == 0) continue;
                
                if (dist[j] > dist[minIndex] + graph[minIndex][j]) {
                    dist[j] = dist[minIndex] + graph[minIndex][j];
                }
            }
        }
    }
}