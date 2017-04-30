"""
Copyright 2017, University of Freiburg,
Chair of Algorithms and Data Structures.
Author: Hannah Bast <bast@cs.uni-freiburg.de>,
        David Leimroth <david.leimroth@jupiter.uni-freiburg.de>
"""


def merge_sort(arr):
    '''Takes an array arr and sorts it

    >>> merge_sort([10])
    [10]

    >>> merge_sort([42, 7, 3, 3, 1])
    [1, 3, 3, 7, 42]

    '''
    if len(arr) <= 1:
        return arr

    length = len(arr)
    size_to_sort = 1

    while size_to_sort < length:
        # do the magic
        left = 0
        while left < length:
            # do the magic
            cond_one = left + size_to_sort * 2
            cond_two = length
            right = cond_one if cond_one < cond_two else cond_two
            arr = merge(arr, left, left + size_to_sort, right)
            # increase size of left
            left += size_to_sort * 2

        # double size_to_sort
        size_to_sort *= 2
    return arr


def merge(arr, left, middle, right):
    '''Merge elements a given lists and points for sublists

    >>> merge([0, 1, 5, 2, 5], 0, 3, 5)
    [0, 1, 2, 5, 5]

    >>> merge([], 0, 0, 1)
    []

    >>> merge([3, 10, 1, 2, 1, 2, 6, 3], 6, 7, 8)
    [3, 10, 1, 2, 1, 2, 3, 6]

    '''
    if len(arr) <= 1:
        return arr
    arr = arr[:]
    arr1 = arr[left:middle]
    arr2 = arr[middle:right]
    temp_arr = []

    arr1len, arr2len = len(arr1), len(arr2)
    itr, itr1, itr2 = 0, 0, 0

    # structure taken from lecture
    while itr1 < arr1len or itr2 < arr2len:
        if itr1 < arr1len and (itr2 == arr2len or arr1[itr1] <= arr2[itr2]):
            temp_arr.append(arr1[itr1])
            itr1 += 1
        if itr2 < arr2len and (itr1 == arr1len or arr2[itr2] <= arr1[itr1]):
            temp_arr.append(arr2[itr2])
            itr2 += 1
        itr += 1
    for i in range(right - 1, left - 1, -1):
        arr[i] = temp_arr.pop()
    return arr


if __name__ == "__main__":
    merge_sort([10, 3, 2, 1, 1, 2, 6, 3])
