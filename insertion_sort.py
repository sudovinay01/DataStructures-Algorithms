# -*- coding: utf-8 -*-
"""

# Insertion Sort
*   Run Time Complexity :
    1.   Worst case : O(n^2)
    2.   List item : Ω(n)
*   Space Complexity : O(1) ---> Only additional space taken by algorithm needs to be considered ignoring input given to the algorithm
"""

import numpy as np

class InsertionSort:
  """
      Class contains different problems on Insertion sort algorithm.
      Author: Siddhi Chaithanya
  """
  def __init__(self, original_array):
    """
    Args:
      original_array: List or array to be sorted
      sorted_array: Array after sorted
      sorted: Boolean to show if array is sorted or not
    """
    self.__original_array = self.__sorted_array = original_array
    self.__sorted = False
    self.__verbose = False

  def apply_insertion_sort(self, verbose=False):
    """
    Args:
      verbose: Boolean to decide if verbose output is required. Default value is False.
    Returns:
      None
    """
    # check if array is already sorted
    if self.__sorted :
      print("Array is already sorted.......")
      return

    self.__verbose = verbose

    # Apply insertion sort algorithm and set sorted = True
    self.__insertion_sort(self.__sorted_array, 0, len(self.__original_array))
    self.__sorted = True

  def __insertion_sort(self, A, L, R):
    """
    Performs insertion sort on given array.
    Args:
      A : Array on which insertion sort to be performed
      L : Arrays left index
      R : Arrays right index
    """
    verbose_output = str("======================================================\nArray to be sorted : {}".format(A))

    for i in range(L+1, R):
      compare_point = A[i]
      j = i-1
      while j >= 0 and A[j] > compare_point:
        A[j+1] = A[j]
        j -= 1
      A[j+1] = compare_point
      verbose_output = "\n".join([verbose_output, str("After first iteration \nIntermediate array : {}".format(A))])

    self.__sorted = True

    if self.__verbose:
      print(verbose_output,"\n======================================================")

  def setOriginalArray(self, original_array):
    """
    Replaces original array with new array
    Args:
      original_array: List or array to be sorted
    """
    self.__original_array = original_array
    self.__sorted_array = original_array
    self.__sorted = False

  def displaySortedArray(self):
    """
    Displays sorted array
    """
    if not self.__sorted :
      print("Array is not sorted yet. Please call apply_insertion_sort() function.......")
      return
    print("Sorted array : ",self.__sorted_array)

i1 = InsertionSort([5,4,3,2,1])
i1.apply_insertion_sort(verbose=True)
i1.displaySortedArray()

i1.setOriginalArray([1,2,3,4,5])
i1.apply_insertion_sort(verbose=True)
i1.displaySortedArray()

