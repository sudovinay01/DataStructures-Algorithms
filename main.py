from search_algorithms.search import Search
from sorting_algorithms.Sort import Sort
from heap.Heap import Heap
import numpy as np

# search example
# s1 = Search([1, 2, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 11, 12, 13, 14])
# print(s1.search(10, kind="binary", occurences="a"))

# sort example
# i1 = Sort([5,4,3,2,1])
# i1.apply(verbose=True)
# i1.displaySortedArray()

# i1.setOriginalArray([1,2,-1,-2,-10,4,5])
# i1.apply(kind="insertion")
# i1.displaySortedArray()

# heap1 = Heap([9, 6, 5, 0, 8, 2, 1, 3])
# heap1.show_heap()

# heap1.heap_insert([4, 10, 15, 23, 1, 56, 103])
# heap1.show_heap()

# print("After sorting: ", heap1.heap_sort())
# heap1.show_heap()
# print(heap1.is_heap(h=[9, 8, 5, 4, 6, 2, 1, 0, 3]))

i1 = Sort(np.array([9, 8, 5, 4, 6, 2, 1, 0, 3, 4, 10, 15, 23, 1, 56, 103]))
i1.apply(kind="quick", verbose=False)
i1.displaySortedArray()

i1.setOriginalArray(np.random.randint(0, 100, size=50))
i1.apply(kind="heap", verbose=False)
i1.displaySortedArray()

i1.setOriginalArray(np.random.randint(0, 100, size=50))
i1.apply(kind="merge", verbose=False)
i1.displaySortedArray()

