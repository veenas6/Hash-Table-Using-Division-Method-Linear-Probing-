class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    # Hash function (division method)
    def hash_function(self, key):
        return key % self.size

    # Insert a key
    def insert(self, key):
        index = self.hash_function(key)
        start_index = index

        while self.table[index] is not None and self.table[index] != "DELETED":
            index = (index + 1) % self.size
            if index == start_index:  # Table is full
                print("Hash table is full. Cannot insert", key)
                return
        self.table[index] = key

    # Search for a key
    def search(self, key):
        index = self.hash_function(key)
        start_index = index

        while self.table[index] is not None:
            if self.table[index] == key:
                return index
            index = (index + 1) % self.size
            if index == start_index:  # Looped back
                break
        return -1

    # Delete a key
    def delete(self, key):
        index = self.search(key)
        if index == -1:
            print(key, "not found.")
        else:
            self.table[index] = "DELETED"
            print(key, "deleted.")

    # Display the table
    def display(self):
        for i in range(self.size):
            print(i, ":", self.table[i])


# ---------------- Example Usage ----------------
ht = HashTable(7)   # hash table of size 7

ht.insert(10)
ht.insert(20)
ht.insert(15)
ht.insert(7)

print("\nHash Table after insertions:")
ht.display()

print("\nSearching 15:", "Found at index" if ht.search(15) != -1 else "Not Found")
print("Searching 99:", "Found at index" if ht.search(99) != -1 else "Not Found")

ht.delete(20)

print("\nHash Table after deleting 20:")
ht.display()
