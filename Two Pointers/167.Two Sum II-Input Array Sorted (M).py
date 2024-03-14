class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Two pointer approach (for sorted array)
        i,j = 0,len(numbers)-1
        #The loop continues until pointers have not crossed eachother
        while i < j:
            Sum = numbers[i] + numbers[j]
            if Sum < target:
                i += 1
            elif Sum > target:
                j -= 1
            else:
                return [i+1,j+1]        
