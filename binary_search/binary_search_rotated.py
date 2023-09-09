from typing import List

def find_min_rotated(arr: List[int]) -> int:
    left = 0
    right = len(arr) - 1

    if arr[left] < arr[right]:
        return left

    while left <= right:
        mid_index = (left + right) // 2
        left_value = arr[mid_index - 1]

        # if the mid index is the rotated value
        if left_value > arr[mid_index]:
            return mid_index
        elif arr[right] > arr[mid_index]:
            # we know the right half is sorted
            right = mid_index - 1
        else:
            left = mid_index + 1

    return 0