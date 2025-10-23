class MinStack {
    List<Integer> minStack = new ArrayList<Integer>();
    public MinStack() {
    }
    
    public void push(int val) {
        minStack.add(val);
    }
    
    public void pop() {
        minStack.remove(minStack.size()-1);
    }
    
    public int top() {
        return minStack.get(minStack.size()-1);
    }
    
    public int getMin() {
        int S=minStack.get(0);
        for(int i=0; i<minStack.size();i++){
            if (minStack.get(i)<S){
                S=minStack.get(i);
            }
        }
        return S;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */