from typing import List 

def binary_search_recursive(arr: List[int], target: int, start=0, end=None) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    if end is None:
        end = len(arr) - 1

    mid_index = (start + end) // 2
    if not arr or (start == end and arr[mid_index] != target):
        return -1
    if arr[mid_index] == target:
        return mid_index
    elif arr[mid_index] < target:
        return binary_search_recursive(arr, target, start=mid_index + 1, end=end)
    elif arr[mid_index] > target:
        return binary_search_recursive(arr, target, start=start, end=mid_index - 1)
    return 0


def binary_search_iterative(arr: List[int], target: int) -> int:
    if not arr:
        return -1

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid_index = (right + left) // 2

        if left == right and arr[mid_index] != target:
            return -1
        if arr[mid_index] == target:
            return mid_index
        elif arr[mid_index] > target:
            # search left side
            right = mid_index - 1
        elif arr[mid_index] < target:
            left = mid_index + 1
