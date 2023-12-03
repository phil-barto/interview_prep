from typing import List

def first_not_smaller(arr: List[int], target: int) -> int:
    left = 0
    right = len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = len(arr) // 2

        if arr[mid] >= target:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return boundary_index

    
def find_first_occurrence(arr: List[int], target: int) -> int:
    left = 0
    right = len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid_index = (left + right) // 2
        current_value = arr[mid_index]

        if current_value == target:
            boundary_index = mid_index
            right = mid_index - 1
        elif current_value > target:
            right = mid_index - 1
        else:
            left = mid_index + 1

    return boundary_index