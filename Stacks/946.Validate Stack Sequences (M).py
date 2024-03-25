class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        arr = []
        while pushed:
            while arr and arr[-1] == popped[0]:
                arr.pop()
                popped.pop(0)
            if pushed:
                arr.append(pushed.pop(0))
        while arr and arr[-1] == popped[0]:
            arr.pop()
            popped.pop(0)
        return not arr
           

                 

