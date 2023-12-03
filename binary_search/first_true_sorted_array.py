
def find_boundary(arr: List[bool]) -> int:
    left = 0
    right = len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = len(arr) // 2

        #true
        if arr[mid]:
            # we see an iteration of true, but not necessarily the first iteration of true
            right = mid - 1
            boundary_index = mid
        # false
        else:
            left = mid + 1

    return mid