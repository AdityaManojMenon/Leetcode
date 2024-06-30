class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        #add val into stack 
        self.stack.append(val)
        #appends val into min_stack if empty or if val is smaller than the last pushed val in min_stack 
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        
    def pop(self) -> None:
        #if stack is not empty pop the top element 
        if self.stack:
            top_val = self.stack.pop()
        #checks if the popped element is the last pushed into min_stack if it is it is the smallest element so needs to be removed 
        if self.min_stack[-1] == top_val:
            self.min_stack.pop()
        
    def top(self) -> int:
        if self.stack:
            top_val = self.stack.pop()
        self.stack.append(top_val)
        return top_val        

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()