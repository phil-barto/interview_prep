from typing import List

def find_boundary_iterative(arr: List[bool]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    for index, bool in enumerate(arr):
        if bool:
            return index
    return -1


def find_boundary_bs(arr: List[bool]) -> int:
    left = 0
    right = len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid_index = (left + right) // 2
        current_value = arr[mid_index]

        if not current_value:
            left = mid_index + 1
        else:
            ## could not be the first iteration of true
            boundary_index = mid_index
            right = mid_index - 1

    return boundary_index
