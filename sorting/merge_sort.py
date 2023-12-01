from typing import List

def sort_list(unsorted_list: List[int]) -> List[int]:
    length_list = len(unsorted_list)

    #base case: list of size 0,1
    if length_list <= 1:
        return unsorted_list

    #split list into 2 recursively
    midpoint = n // 2

    left_list = sort_list(unsorted_list[:midpoint])
    right_list = sort_list(unsorted_list[midpoint:])

    result_list = []
    left_pointer = 0
    right_pointer = 0

     # Merge the sorted left and right lists with two pointers
    while left_pointer < midpoint or right_pointer < n - midpoint:
        # if left list is empty
        if left_pointer == midpoint: 
            result_list.append(right_list[right_pointer])
            right_pointer += 1
        # if right list is empty
        if right_pointer == midpoint:
            result_list.append(left_list[left_pointer])
            left_pointer += 1
        if left_list[left_pointer] <= right_list[right_pointer]:
            result_list.append(left_list[left_pointer])
            left_pointer += 1
        else:
            result_list.append(right_list[right_pointer])
            right_pointer += 1
    
    return result_list