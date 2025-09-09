🔑Simple Hash Table Implementation in Python
This repository contains a straightforward Hash Table implementation using open addressing with linear probing for collision resolution.

💡 Overview
This Python class demonstrates:
1. Hashing using the division method:
The key is hashed by taking the modulo with the table size.
2. Collision handling with linear probing:
If a collision occurs, the algorithm searches sequentially for the next available slot.
3. Basic operations:
Insert, search, delete, and display keys in the hash table.

📚 Features
Operation	Description
insert	Adds a key to the hash table
search	Searches for a key and returns its index or -1 if not found
delete	Deletes a key by marking the slot as "DELETED"
display	Prints the current state of the hash table

🚀 How to Use
ht = HashTable(7)  # Create a hash table of size 7
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

🖥️ Sample Output
Hash Table after insertions:
0 : None
1 : 15
2 : 7
3 : None
4 : 10
5 : 20
6 : None

Searching 15: Found at index
Searching 99: Not Found
20 deleted.

Hash Table after deleting 20:
0 : None
1 : 15
2 : 7
3 : None
4 : 10
5 : DELETED
6 : None

🔍 How It Works
Hash Function:
hash_function(key) = key % size

Linear Probing:
If a slot is occupied or marked as "DELETED", try the next slot (circularly) until an empty one is found.

Deletion:
Instead of clearing the slot, the key is replaced with a "DELETED" marker to avoid breaking the probing chain during searches.

✨ Why Use This?
Easy to understand demonstration of hash tables with collision handling.
Useful for learning hashing concepts and open addressing techniques.
Great starter code to extend with features like dynamic resizing or different probing methods.
