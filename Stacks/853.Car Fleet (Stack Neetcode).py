class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Alternatively we could have created a hashmap
        pair = [(p,s) for p,s in zip(position,speed)]
        stack = []
        for p,s in sorted(pair)[::-1]: #Reverse sorted order (Traversing backwards)
            stack.append((target-p)/s)
            if len(stack) >= 2 and (stack[-1] <= stack[-2]):
                stack.pop()
        return len(stack)       
