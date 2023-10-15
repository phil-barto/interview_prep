# Table of Contents

## Stacks

First In Last Out.

Supports 3 operations:
- push
- peek
- pop

## Queue
First in First Out
Last in Last Out

Supports 3 operations:
- Insert (or "Push"): Putting an item into the end of the queue.
- Peek: Look at the first item of the queue.
- Remove (or "Pop"): Remove the first item of the queue.

## Hashmap
Basically a dictionary. Just a way to map values to certain keys, etc.

### Hash Function
Converts data of arbitrary size to a value of fixed size. 

For example, a simple hash function for an integer array can be one that sums up each entry in the array and modulo the sum by 100. Hashing [5, 23, 84] returns (5 + 23 + 84) % 100 = 12, while hashing [31, 22, 45, 61, 10] returns (31 + 22 + 45 + 61 + 10) % 100 = 69. In this example, the hash function converts an arbitrarily large data structure (arbitrary sized array with arbitrary sized integers as entries) and turns it into a fixed sized value (an integer with only 100 possible values).

### Efficiency
 The average time complexity is O(n / k) for each insertion/access operation on the table, where n is the number of entries in the hash table and k is the array size of the table. This is because of the pigeonhole principle.

