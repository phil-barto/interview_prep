from typing import List

def sort_list(unsorted_list: List[int]) -> List[int]:
    length = len(unsorted_list)
    for index, num in enumerate(unsorted_list):
        for i in range(index):
            if unsorted_list[i + 1] < unsorted_list[i]:
                unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1], unsorted_list[i]
    
    return unsorted_list

print(sort_list([12, 11, 13, 5, 6]))