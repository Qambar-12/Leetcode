#we are required  to create a dictionary or hashmap with keys and value pointing to nodes
#the size of the dictionary must not exceed the capacity
#after each get or put operation we need to to change the LRU node and most recently used node
#these swapping of nodes require a doubly linked list having both a prev and next pointer
#this node also has a value which in this case holds (key,val) to which hashmap's key is pointing to
class Node:
    def __init__(self,key,val):
        self.key , self.val = key , val
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}         #hashmap that maps key to node
        #dummy nodes for LRU and most recently used
        self.left , self.right = Node(0,0) , Node(0,0)
        #initially connected nodes so that we can insert in between those
        self.left.next , self.right.prev = self.right , self.left
    
    #remove (middle) node from list (connecting the pointers)
    def remove(self,node):
        prev , nxt = node.prev , node.next
        prev.next , nxt.prev = nxt , prev
    #insert node to right (connecting the pointers)
    def insert(self,node):
        prev , nxt = self.right.prev , self.right
        prev.next = nxt.prev = node
        node.next , node.prev = nxt , prev  
    def get(self, key: int) -> int:
        if key in self.cache:
            #use of helper functions (remove and insert to move it to right most position)
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        #now we need to create a new node
        self.cache[key] = Node(key,value)
        #now insert inside the doubly linked list
        self.insert(self.cache[key])
        #check for capacity
        if len(self.cache) > self.cap:
            #remove LRU from list and delete it from hashmap cache aswell
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
