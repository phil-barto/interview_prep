from typing import List

def find_first_occurrence(arr: List[int], target: int) -> int:
    l, r = 0, len(arr) - 1
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            ans = mid
            r = mid - 1
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return ans