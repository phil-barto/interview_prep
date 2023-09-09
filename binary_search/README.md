# Binary Search

## Vanilla Binary Search

- Searching through sorted list, using the middle index and then searching the half to the left or right
- Need some error checking for invalid inputs
    - Empty list, if out of range
Think about the edge cases
- If the element is past the list
- iterative is probably the way to go here, since recursion you have to pass the start / end in the call traces
- Time: O(logn)
- Space: O(1) iterative, O(logn) recursive

## Sorted Binary Search

- https://algo.monster/problems/binary_search_boundary 
- Find first element of True
- First start simple, just loop
- Binary search
    - Bit more complex because the first iteration of true we see isn’t necessarily the first iteration of True
    - Keep a variable boundary_index, which is the first iteration of true, if the left is greater than the right then return boundary index

## Binary Search - Duplicates
- https://algo.monster/problems/binary_search_duplicates
- Very similar to the sorted boolean array and vanilla binary search
- Research feasible function

## Min in rotated sorted array
- https://algo.monster/problems/min_in_rotated_sorted_array
- Key is searching for a boolean expression
- The key here is to look at the left and right values to determine if the left/right sides are sorted.
- mistakes:
    - not doing `left <= right` rather than `left < right`
    - use paranthesis when doing mathmatical operations
        - `left + right // 2` is **not** the correct way
        - `(left + right) // 2` is **the** correct way

## Mountain Peak
- https://algo.monster/problems/peak_of_mountain_array
- key is to look at the value to the left, and the value to the right
- if the value to the right is **greater** than the mid index, we know the peak must be to the right
- if the value to the left is **greater** than the mid index, we know the peak must be to the left
- 