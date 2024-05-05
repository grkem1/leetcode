// https://leetcode.com/problems/design-hashmap


class MyHashMap:

    bucketSize = 0
    myTable = []

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucketSize = 1000
        self.myTable = [[]]*self.bucketSize

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        bucket = hash(key)%self.bucketSize
        for i in range(len(self.myTable[bucket])):
            if(self.myTable[bucket][i][0] == key):
                self.myTable[bucket][i][1] = value
                return
        self.myTable[bucket].append([key,value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        bucket = hash(key)%self.bucketSize
        for i in range(len(self.myTable[bucket])):
            if(self.myTable[bucket][i][0] == key):
                return self.myTable[bucket][i][1]
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        bucket = hash(key)%self.bucketSize
        for i in range(len(self.myTable[bucket])):
            if(self.myTable[bucket][i][0] == key):
                del(self.myTable[bucket][i])
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
