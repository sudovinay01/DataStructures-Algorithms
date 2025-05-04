from search_algorithms.search import Search
import numpy as np

# linear search example
s1 = Search([1, 2, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 11, 12, 13, 14])
print(s1.search(10, kind="binary", occurences="a"))