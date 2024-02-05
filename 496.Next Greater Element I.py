class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums1)):
            index = nums2.index(nums1[i])
            print(index)
            if index != len(nums2)-1:
                List = nums2[index+1:]
                for element in List:
                    if element > nums1[i]:
                        ans.append(element)
                        break
                else:
                    ans.append(-1)
            else:
                ans.append(-1) 
        return ans               

