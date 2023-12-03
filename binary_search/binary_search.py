
def binary_search_iterative(arr: List[int], target: int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = len(arr) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] > targat:
            right = mid - 1

        if arr[mid] < target:
            left = mid + 1

    return -1

def binary_search_recursive(arr: List[int], target: int, left: int, right: int) -> int:
    mid = len(arr) // 2  
    
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    if arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)