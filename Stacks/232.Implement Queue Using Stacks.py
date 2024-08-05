class MyQueue:

    def __init__(self):
        #two stacks to achieve approximately const time complexity O(1) to simulate queue 
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)


    def pop(self) -> int:
        #because stack2 holds the elements in reverse order i.e elements first popped from stack1 and then pushed into stack2
        if self.stack2 :
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop() 
    def peek(self) -> int:
        if self.stack2 :
            return self.stack2[-1]
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1]   

    def empty(self) -> bool:
        if self.stack1 or self.stack2:
            return False
        return True    


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
