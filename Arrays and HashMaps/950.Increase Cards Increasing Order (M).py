class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        #intial sorting 
        deck.sort()
        #using queue as data structure we need to skip indices by pushing to back and popping from front of queue
        res = [0] * len(deck)
        #queue containing indices we need to alternately fill res array
        q = deque(range(len(deck)))
        for card in deck:
            index = q.popleft()
            res[index] = card
            if q:
                q.append(q.popleft())
        return res        
