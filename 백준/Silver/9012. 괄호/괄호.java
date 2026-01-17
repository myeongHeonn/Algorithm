import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringBuilder sb = new StringBuilder();
        
        int t = Integer.parseInt(br.readLine());
    	
    	for (int test_case = 1; test_case < t + 1; test_case++) {
    		String line = br.readLine();
    		Stack<Character> stack = new Stack<>();
    		boolean isValid = true;
    		
    		for (int i = 0; i < line.length(); i++) {
    			char c = line.charAt(i);
    			
    			if (c == '(') {
    				stack.push(c);
    			} else {
    				if (!stack.empty()) {
    					stack.pop();
    				} else {
    					isValid = false;
    					break;
    				}
    			}
    		}
    		if (!stack.empty()) {
    			isValid = false;
    		}
    		if (isValid) {
    			sb.append("YES\n");
    		} else {
    			sb.append("NO\n");
    		}
    	}
    	System.out.println(sb);
    }
}