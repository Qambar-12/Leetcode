class MyHashSet:

    #constructor initializes the instance of hashset to an array
    #simulating behaviour of hashset using an array
    def __init__(self):
        self.hashset = []

    def add(self, key: int) -> None:
        #Because set cannot have duplicates
        if key not in self.hashset:
            self.hashset.append(key)

    def remove(self, key: int) -> None:
        if key in self.hashset:
            self.hashset.remove(key)

    def contains(self, key: int) -> bool:
        return True if key in self.hashset else False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
