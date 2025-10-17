import java.util.Stack;
class Solution {
   public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        char[] S = s.toCharArray();
        if (S.length %2!=0){return false;}
        for (int i = 0; i < s.length(); i++) {
            if (S[i] == '{' || S[i] == '(' || S[i] == '[') {
                stack.push(S[i]);
            }else{
                if(stack.empty()) return false;
                switch (S[i]){
                    case ')': if(stack.peek()=='('){stack.pop();}else{ return false;};
                        break;
                    case ']': if(stack.peek()=='['){stack.pop();}else{ return false;};
                        break;
                    case '}': if(stack.peek()=='{'){stack.pop();}else{ return false;};
                        break;
                    default: return false;
                }
            }
        }
        return stack.empty();
    }
}