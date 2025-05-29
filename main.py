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

heap1 = Heap([9, 6, 5, 0, 8, 2, 1, 3])
heap1.show_heap()

heap1.heap_insert(4)
heap1.show_heap()

print(heap1.check_max_heap())