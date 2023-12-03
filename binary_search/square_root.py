
def square_root(n: int) -> int:
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if (mid ** 2) == n:
            return mid
        elif (mid ** 2) > n:
            right = mid - 1
        else:
            left = mid + 1
