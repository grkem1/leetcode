# https://leetcode.com/problems/design-hashset

class MyHashSet:

    def __init__(self):
        self.set = []

    def add(self, key: int) -> None:
        self.set += [False] * (key - len(self.set) + 1)
        self.set[key] = True

    def remove(self, key: int) -> None:
        if(self.contains(key)):
            self.set[key] = False

    def contains(self, key: int) -> bool:
        return len(self.set) > key and self.set[key] == True


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)