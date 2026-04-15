import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        
        int n = Integer.parseInt(br.readLine());
        
        ArrayList<Integer> list = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
        	st = new StringTokenizer(br.readLine());
        	
        	String command = st.nextToken();
        	
        	if (command.equals("push_back")) {
        		int num = Integer.parseInt(st.nextToken());
        		list.add(num);
        	}
        	else if (command.equals("pop_back")) {
        		list.remove(list.size() - 1);
        	}
        	else if (command.equals("size")) {
        		sb.append(list.size()).append("\n");
        	}
        	else if (command.equals("get")) {
        		int index = Integer.parseInt(st.nextToken());
        		sb.append(list.get(index - 1)).append("\n");
        	}
        }
        
        System.out.println(sb);
    }
}