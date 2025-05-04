from search_algorithms.search import Search
import numpy as np

# linear search example
s1 = Search(np.array([1, 2, 7, 7, 7, 10]))
print(s1.search(7, kind="binary", occurences="a"))