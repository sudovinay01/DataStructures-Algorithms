# Data Structures And Algorithms

This Python project is created with the intention of covering all the fundamental data structures and algorithms, making it a helpful resource for anyone starting their journey into DSA.  
Currently, it includes searching and sorting techniques — with many more to come!


## ✨ Features

- 🔍 Searching algorithms:
  - Linear Search (first, last and all occurences)
  - Binary Search (first, last and all occurences)

- 🔃 Sorting algorithms:
  - Bubble Sort (with verbose option)
  - Selection Sort (with verbose option)
  - Insertion Sort (with verbose option)
  - Merge Sort (with verbose option)
  - Quick Sort (with random pivot verbose option)

## How to use?
Please look into file main.py for its usage
1. For search
   - s1 = Search([1, 2, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 11, 12, 13, 14])
   - print(s1.search(10, kind="binary", occurences="a"))
   - kind : linear|l, binary|b ---> case insensitive
2. For sorting
   - i1 = Sort([5,4,3,2,1])
   - i1.apply(verbose=True)
   - i1.displaySortedArray()
   - i1.setOriginalArray([1,2,-1,-2,-10,4,5])
   - i1.apply(kind="insertion")
   - i1.displaySortedArray()
   - kind : quick_random|q_r, merge|m, selection|s, insertion|i, bubble|b ---> case insensitive

## 📦 Installation

Clone the repository:

```bash
git clone [https://github.com/your-username/DSA-Algorithms-Python.git](https://github.com/AumaujayaSiddhi/DataStructures-Algorithms)
cd DataStructures-Algorithms


