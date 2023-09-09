from typing import List

def binary_search_mountain_peak(arr: List[int]) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid_index = (left + right) // 2
        value_right_of_mid = arr[mid_index + 1]
        value_left_of_mid = arr[mid_index - 1]
        
        if value_left_of_mid < arr[mid_index] and arr[mid_index] > value_right_of_mid:
            return mid_index
        elif value_right_of_mid > arr[mid_index]:
            left = mid_index + 1
        elif value_left_of_mid > arr[mid_index]:
            right = mid_index - 1