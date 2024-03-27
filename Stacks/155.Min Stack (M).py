class MinStack:

    def __init__(self):
        #Using array in place of stack in python and creating addition array minStack that keeps track of min at every stage 
        #O(1) time complexity of each function operation
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        #we need to pop from minStack aswell because it keeps track of min at every level
        self.stack.pop()
        self.minStack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
