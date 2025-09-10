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
            if index == start_index:
                print("Hash table is full. Cannot insert", key)
                return
        self.table[index] = key
        print("Inserted", key)

    # Search for a key
    def search(self, key):
        index = self.hash_function(key)
        start_index = index

        while self.table[index] is not None:
            if self.table[index] == key:
                return index
            index = (index + 1) % self.size
            if index == start_index:
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
        print("\nHash Table:")
        for i in range(self.size):
            print(i, ":", self.table[i])
        print()


# ----------- Menu-Driven Program -----------
def main():
    size = int(input("Enter the size of the hash table: "))
    ht = HashTable(size)

    while True:
        print("\n==== Hash Table Menu ====")
        print("1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Display")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            key = int(input("Enter key to insert: "))
            ht.insert(key)

        elif choice == '2':
            key = int(input("Enter key to search: "))
            index = ht.search(key)
            if index != -1:
                print("Key found at index:", index)
            else:
                print("Key not found.")

        elif choice == '3':
            key = int(input("Enter key to delete: "))
            ht.delete(key)

        elif choice == '4':
            ht.display()

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


# Run the program
if __name__ == "__main__":
    main()

