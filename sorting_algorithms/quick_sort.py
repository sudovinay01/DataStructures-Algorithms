# -*- coding: utf-8 -*-
"""
Description : Different problems on quick sort algorithm
Author : Siddhi Chaithanya
*   Run Time Complexity : Average Case : θ(nlogn), Worst Case: O(n^2)
*   Space Complexity : O(logn) ---> Only additional space taken by algorithm needs to be considered ignoring input given to the algorithm

"""

import numpy as np

class QuickSort:
  """
      Class contains different problems on quick sort algorithm.
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

  def apply_quick_sort(self, randomPivot=False, verbose=False):
    """
    Args:
      randomPivot: Boolean to decide if pivot element should be selected. Default value is False.
      verbose: Boolean to decide if verbose output is required. Default value is False.
    Returns:
      None
    """
    # check if array is already sorted
    if self.__sorted :
      print("Array is already sorted.......")
      return

    self.__verbose = verbose

    # Apply quick sort algorithm and set sorted = True
    self.__quick_sort(self.__sorted_array, 0, len(self.__original_array)-1, randomPivot)
    self.__sorted = True

  def __quick_sort(self, A, L, R, random_pivot):
    """
    Performs quick sort on given array.
    Args:
      A : Array on which quick sort to be performed
      L : Arrays left index
      R : Arrays right index
      random_pivot : booean value to decide picking of pivot element
    """
    if L < R :
      pivot_index = self.__pivot_placement(A, L, R, random_pivot)
      self.__quick_sort(A, L, pivot_index - 1, random_pivot)
      self.__quick_sort(A, pivot_index + 1, R, random_pivot)

    self.__sorted = True

  def __pivot_placement(self, A, L, R, random_pivot):
    """
      Choose pivot and find its right place in the array.
      Pivot can be choosen as the element at last index or randomly.
      Args:
        A : Array on which pivot placement to be found
        L : Arrays left index
        R : Arrays right index
        random_pivot : booean value to decide picking of pivot element
    """
    verbose_output = str("======================================================\nArray : {}, Left Index : {}, Right Index : {}".format(A[L:R+1], L, R))

    if random_pivot:
      rand_index = np.random.randint(L, R)
      verbose_output = "\n".join([verbose_output, str("Random pivot index : {}".format(rand_index)), str("Random pivot element : {}".format(A[rand_index]))])
      (A[R], A[rand_index]) = (A[rand_index], A[R])
    else:
      verbose_output = "\n".join([verbose_output, str("Pivot index : {}\nPivot element : {}".format(R, A[R]))])
    
    pivot_element = A[R]
    left_movement = L-1
    right_movement = L

    while right_movement < R:
      if A[right_movement] <= pivot_element:
        left_movement += 1
        (A[left_movement], A[right_movement]) = (A[right_movement], A[left_movement])
      right_movement += 1

    (A[left_movement+1], A[R]) = (A[R], A[left_movement+1])

    verbose_output = "\n".join([verbose_output, str("Correct pivot index : {}".format(left_movement+1)), str("Left partition : {}".format(A[L:left_movement+1])), str("Right partition : {}".format(A[left_movement+2:R+1]))])
    if self.__verbose:
      print(verbose_output,"\n======================================================")

    return left_movement + 1

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
      print("Array is not sorted yet. Please call apply_quick_sort() function.......")
      return

    print("Sorted array : ",self.__sorted_array)

qs1 = QuickSort(np.random.randint(1, 20, size=21))
qs1.apply_quick_sort(randomPivot=True, verbose=True)

qs1.apply_quick_sort(randomPivot=True)

qs1.displaySortedArray()

qs1.setOriginalArray([2, 5, 20, 15, 4, 1, 0.5, 1.8])
qs1.apply_quick_sort(randomPivot=True)
qs1.displaySortedArray()

qs1.setOriginalArray([2, 5, 20, 15, 4, 1, 0.5, 1.8])
qs1.apply_quick_sort(randomPivot=True, verbose=True)
qs1.displaySortedArray()

qs1.setOriginalArray([2, 5, 20, 15, 4, 1, 0.5, 1.8])
qs1.apply_quick_sort(verbose=True)
qs1.displaySortedArray()

