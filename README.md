# 🔐 Hash Table Implementation (Python)

## 📌 Overview  
This Python program provides a simple implementation of a **hash table** using **open addressing with linear probing**. It allows the user to perform the following operations through a **menu-driven interface**:

- Insert keys  
- Search for keys  
- Delete keys  
- Display the current state of the hash table

It's designed to demonstrate core hashing concepts in an interactive, beginner-friendly way.

---

## ⚙️ Features

✅ **Efficient Insertion**  
Uses the division method (`key % size`) to determine the index for inserting keys. Collisions are handled using **linear probing**.

🔍 **Key Search**  
Finds and returns the index of a key if present; otherwise, notifies the user that the key is not found.

🗑️ **Deletion with "DELETED" Marker**  
Keys can be deleted logically by marking them as `"DELETED"` instead of removing them outright — ensuring the integrity of subsequent search operations.

📊 **Visual Display of Hash Table**  
Displays the current contents of the hash table, including empty and deleted slots, making it easy to understand the table’s state.

---

## 🏗️ Technologies Used

- **Language**: Python 3  
- **Concepts**:  
  - Hash Functions (Division Method)  
  - Open Addressing  
  - Linear Probing  
  - Menu-Driven Programming

---

## ▶️ How to Run

1. Ensure Python 3 is installed on your system.  
2. Save the code to a file, for example: `hash_table.py`  
3. Open a terminal and run the program:

```bash
python hash_table.py
