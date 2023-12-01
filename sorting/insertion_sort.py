from typing import List

def sort_list(unsorted_list: List[int]) -> List[int]:
    length = len(unsorted_list)
    # start at second index
    for index, value in enumerate(unsorted_list, start=1):
        # look at value to the left
        current = index - 1
        # if value to the left is smaller, swap with current
        while current > 0 and unsorted_list[current] < unsorted_list[current-1]:
            unsorted_list[current - 1], unsorted_list[current] = unsorted_list[current], unsorted_list[current - 1]
            current -= 1
        
    return unsorted_list

print(sort_list([12, 11, 13, 5, 6]))