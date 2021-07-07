class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table={}

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.table[key] = value
        return

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if not key in self.table:
            return -1
        return self.table[key]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.table[key]=-1
        return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)