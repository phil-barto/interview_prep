from typing import List

def sort_list(unsorted_list: List[int]) -> List[int]:
    length = len(unsorted_list)
    for index, num in enumerate(unsorted_list):
        temp_index = index
        
        for i in range(index, length):
            if unsorted_list[i] < unsorted_list[temp_index]:
                temp_index = i 

        unsorted_list[index], unsorted_list[temp_index] = unsorted_list[temp_index], unsorted_list[index]

    return unsorted_list

print(sort_list([12, 11, 13, 5, 6]))