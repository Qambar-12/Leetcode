class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Dictionary to store counts of elements
        counts = {}
        # Variable to count the number of operations
        operations = 0 
        # Iterate through the array
        for num in nums:
            # Calculate the complement that would sum to k with the current number
            diff = k - num 
            # Check if the complement exists in the counts dictionary and has a positive count
            if diff in counts and counts[diff] > 0:
                # We found a pair
                operations += 1
                # Decrease the count of the complement since we've used it
                counts[diff] -= 1
            else:
                # Increase the count of the current number
                if num in counts:
                    counts[num] += 1
                else:
                    counts[num] = 1
        
        # Return the number of operations (pairs found)
        return operations
