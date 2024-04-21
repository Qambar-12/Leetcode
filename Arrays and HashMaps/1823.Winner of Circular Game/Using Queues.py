class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        #Solution using the queue data structure. Move in a circle to brings the person at the top of queue to remove 
        q= deque([x+1 for x in range(n)])
        while len(q) > 1:
            c=k-1
            while c:
                q.append(q.popleft())
                c-=1
            q.popleft()
        return q[0]