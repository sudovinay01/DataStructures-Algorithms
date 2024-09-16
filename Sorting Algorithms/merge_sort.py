# -*- coding: utf-8 -*-
"""

# Merge Sort


*   Run Time Complexity :

    Average case : θ(nlogn)

*   Space Complexity : O(n+logn) logn is for stack and n is for extra space for temp array as part of merge function, So overall time complexity is O(n)
"""

import numpy as np

class MergeSort:
  """
      Class contains different problems on merge sort algorithm.
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

  def apply_merge_sort(self, verbose=False):
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

    # Apply merge sort algorithm and set sorted = True
    self.__merge_sort(self.__sorted_array, 0, len(self.__original_array)-1)
    self.__sorted = True

  def __merge_sort(self, A, L, R):
    """
    Performs merge sort on given array.
    Args:
      A : Array on which merge sort to be performed
      L : Arrays left index
      R : Arrays right index
    """
    division_point = (L+R-1)//2
    if L < R :
      self.__merge_sort(A, L, division_point)
      self.__merge_sort(A, division_point+1, R)
      self.__merge(A, L, division_point, R)

  def __merge(self, A, L, division_point, R):
    """
      Merge two individual arrays into 1 sorted array
      Args:
        A : Array on which merge to be performed
        L : Arrays left index
        division_point : Arrays division point
        R : Arrays right index
    """
    verbose_output = str("======================================================\nArray : {}, Left Index : {}, Right Index : {}".format(A[L:R+1], L, R))

    A_temp = list()
    first_index = L
    second_index = division_point + 1
    while first_index <=division_point and second_index <= R :
      if A[first_index] < A[second_index] :
        A_temp.append(A[first_index])
        first_index += 1
      else :
        A_temp.append(A[second_index])
        second_index += 1

    if first_index <= division_point :
      for i in range(first_index, division_point+1) :
        A_temp.append(A[i])
    if second_index <= R :
      for i in range(second_index, R+1) :
        A_temp.append(A[i])

    for i in range(L, R+1) :
      A[i] = A_temp[i-L]

    verbose_output = "\n".join([verbose_output, str("Merged array : {}\nTemp array : {}".format(A, A_temp))])
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
      print("Array is not sorted yet. Please call apply_merge_sort() function.......")
      return
    print("Sorted array : ",self.__sorted_array)

m1 = MergeSort([5,4,3,2,1])
m1.apply_merge_sort(verbose=True)
m1.displaySortedArray()

m1.setOriginalArray([25, 4, 4, 100, 0, -1, 15, 150])
m1.apply_merge_sort(verbose=True)
m1.displaySortedArray()

