# Sorting

## Introduction
- Stable sorting algorithm
    - relative order is maintaind when two entries with the same value occur
- In-place memory algorithm
    - algorithm doesn't use any additional data structures to hold temporary data


## Insertion Sort
Only the first item in the list is considered sorted. Then, for each item in the sequence, we insert the item in the list by swapping it with the item before it until the item is smaller than the current item. 

[Example](https://www.youtube.com/watch?v=JU767SDMDvA)

``` #type: python
def sort_list(unsorted_list: List[int]) -> List[int]:
    for i, entry in enumerate(unsorted_list):
        current = i
        # gets the smallest element and inserts it at current index 
        while current > 0 and unsorted_list[current] < unsorted_list[current - 1]:
            # swaps current smaller element with the element before it
            unsorted_list[current], unsorted_list[current - 1] = unsorted_list[current - 1], unsorted_list[current]
            current -= 1
    return unsorted_list
```

### Complexity
Time complexity:
- For each `n` item in the list, the time complexity to sort it is `i` where `i` is the index of that item. The complexity becomes `O(n ( n - i) / 2)`

Memory complexity:
- Because the memory stays and there's only a temporary variable, the memory is `O(n)`

## Selection Sort

We find the smallest item from the unsorted pile and add it to the sorted pile.

By finding the smallest element, we use a temporary variable keeping track of the index. We compare each element in the unsorted pile and update the new index if necessary.

After all the elements have been compared, swap the element with the smallest index with the first element of the unsorted pile. 

``` #type: python
def sort_list(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list)
    for i in range(n):
        # Assume the current position as minimum
        min_index = i

        # Find the minimum element's index from the rest of the list
        for j in range(i, n):
            if unsorted_list[j] < unsorted_list[min_index]:
                min_index = j

        # Swap the minimum element with the first element
        unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]
    return unsorted_list
```

### Complexity
Time complexity: `O(n^2)`
Not stable

## Bubble Sort

For each pass, use a pointer to point to the first element of a life. For each cycle, compare it to the next element in the list and swap them if the current item is greater. Move the pointer bye one until it reaches the end of the list. Largest element always "floats" to the top during each pass. 

``` #type: python
def sort_list(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list)
    for i in range(n):
        # Assume the current position as minimum
        min_index = i

        # Find the minimum element's index from the rest of the list
        for j in range(i, n):
            if unsorted_list[j] < unsorted_list[min_index]:
                min_index = j

        # Swap the minimum element with the first element
        unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]
    return unsorted_list
```

### Complexity
- Time complexity: `O(n^2)`
- Space complexity: `O(n)`


## Merge Sort
Divide and conquer. Divide the array into 2 equally distant lists and sort them.  Have two pointers point to the bottom of the two lists. Compare and then add up.

``` #type: python
def sort_list(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list)

    # Base case: A list of size 1 or 0 is already sorted
    if n <= 1:
        return unsorted_list

    # Split the list into left and right halves
    midpoint = n // 2
    left_list, right_list = sort_list(unsorted_list[:midpoint]), sort_list(unsorted_list[midpoint:])
    
    result_list = []
    left_pointer, right_pointer = 0, 0

    # Merge the sorted left and right lists with two pointers
    while left_pointer < midpoint or right_pointer < n - midpoint:
        if left_pointer == midpoint:  # If left list is empty, append element from right
            result_list.append(right_list[right_pointer])
            right_pointer += 1
        elif right_pointer == n - midpoint:  # If right list is empty, append element from left
            result_list.append(left_list[left_pointer])
            left_pointer += 1
        elif left_list[left_pointer] <= right_list[right_pointer]:  # Append smaller element from left
            result_list.append(left_list[left_pointer])
            left_pointer += 1
        else:  # Append smaller element from right
            result_list.append(right_list[right_pointer])
            right_pointer += 1

    return result_list
```

### Time Complexity
Time Complexity: `O(nlogn)`

## Quick Sort

We select an arbitrary element in the list (known as the "pivot"), and we swap the elements in the list into two sides: a side where all the elements are smaller than the pivot, and a side where all the elements are larger or equal to the pivot.

How would it group? One of the ways to achieve this is that for the interval that we are sorting, we have a pointer point before the start and at the end (including the pivot). For each swap, we move the start pointer until we find an element larger or equal to the pivot (after the initial index) and move the end pointer until we find an element smaller or equal to the pivot (before the initial index). Then we can swap those two elements and restart the process. If those two pointers meet, we stop , and then we can swap the pivot and the meeting point.

```
def sort_list_interval(unsorted_list: List[int], start: int, end: int) -> None:
    # If segment is 1 or 0, it's sorted
    if end - start <= 1:
        return

    # Using last element as the pivot
    pivot = unsorted_list[end - 1]
    start_ptr, end_ptr = start, end - 1

    # Partitioning process
    while start_ptr < end_ptr:
        # Find the next element from the left that is larger than the pivot
        while unsorted_list[start_ptr] < pivot and start_ptr < end_ptr:
            start_ptr += 1
        
        # Find the next element from the right that is smaller than or equal to the pivot
        while unsorted_list[end_ptr] >= pivot and start_ptr < end_ptr:
            end_ptr -= 1

        # Swap if pointers haven't met
        unsorted_list[start_ptr], unsorted_list[end_ptr] = unsorted_list[end_ptr], unsorted_list[start_ptr]

    # Place pivot in its final position
    unsorted_list[start_ptr], unsorted_list[end - 1] = unsorted_list[end - 1], unsorted_list[start_ptr]

    # Sort left and right of the pivot
    sort_list_interval(unsorted_list, start, start_ptr)
    sort_list_interval(unsorted_list, start_ptr + 1, end)

def sort_list(unsorted_list: List[int]) -> List[int]:
    sort_list_interval(unsorted_list, 0, len(unsorted_list))
    return unsorted_list

```