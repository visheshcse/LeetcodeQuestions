//https://leetcode.com/problems/valid-parentheses/

class Solution {
    public boolean isValid(String s) {
        String parenthesis = s;
        Stack<Character> stack = new Stack<>();
        for(int i = 0; i < parenthesis.length(); i++){
            if(parenthesis.charAt(i) == '(' || parenthesis.charAt(i) == '[' || parenthesis.charAt(i) == '{'){
                stack.push(parenthesis.charAt(i));
            }
            else if (parenthesis.charAt(i) == ')' && !stack.empty() && '(' == stack.peek()) {
                stack.pop();
            }
            
            else if (parenthesis.charAt(i) == ']' && !stack.empty() && '[' == stack.peek()) {
                stack.pop();
            }
            
            else if (parenthesis.charAt(i) == '}' && !stack.empty() && '{' == stack.peek()) {
                stack.pop();
            }
            else{
                return false;
            }
            
        }
        return stack.empty();
        
    }
}