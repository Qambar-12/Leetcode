class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0] * n  # Initialize the result array to store visible counts for each person
        stack = []  # Stack to keep track of indices of people in decreasing height order

        # Traverse the queue from left to right
        for i, h in enumerate(heights):
            # While stack is not empty and current person is taller than the top of the stack
            # it means the person at stack[-1] can see the current person (i.e., person i)
            while stack and heights[stack[-1]] < h:
                res[stack.pop()] += 1  # Pop the shorter person and increment their count

            # If stack is not empty, it means the person on top of the stack is taller,
            # so they can see the current person 
            if stack:
                res[stack[-1]] += 1  # The person at stack[-1] can see current person i

            # Push current person's index onto the stack for future comparisons
            stack.append(i)

        return res
