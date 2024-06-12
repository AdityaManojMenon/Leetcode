class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        if not self.empty():
            while len(self.stack1) > 1:
                n = self.stack1.pop()
                self.stack2.append(n)
            x = self.stack1.pop()
            while self.stack2:
                a = self.stack2.pop()
                self.stack1.append(a)
            return x
            
        
    def peek(self) -> int:
        if not self.empty():
            while len(self.stack1) > 1:
                n = self.stack1.pop()
                self.stack2.append(n)
            x = self.stack1.pop()
            self.stack2.append(x)
            while self.stack2:
                a = self.stack2.pop()
                self.stack1.append(a)
            return x
        

    def empty(self) -> bool:
        if len(self.stack1) == 0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()