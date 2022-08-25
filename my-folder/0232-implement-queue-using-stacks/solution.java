import java.util.Stack;

class MyQueue {
    
    private Stack<Integer> input;
    private Stack<Integer> output;

    public MyQueue() {
        input = new Stack<>();
        output = new Stack<>();
    }
    
    public void push(int x) {
        input.push(x);
        System.out.println("Input: " + input);
    }
    
    public int pop() {
        if (output.isEmpty()) {
            while (!input.isEmpty()) {
                int new_int= input.pop();
                output.push(new_int);
            }
        }
        return output.pop();
    }
    
    public int peek() {
        if (output.isEmpty()) {
            while (!input.isEmpty()) {
                int new_int= input.pop();
                output.push(new_int);
            }
        }
        return output.peek();
    }
    
    public boolean empty() {
        return output.isEmpty() && input.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */