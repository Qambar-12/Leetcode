class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        arr = []
        #all elements that appear twice would be removed from arr except for the element that appear once only
        for i in nums :
            if i not in arr:
                arr.append(i)
            else:
                arr.remove(i)
        return arr[0]            
