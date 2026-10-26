import sys

input = sys.stdin.readline
print = sys.stdout.write

def get_upper(arr, target):
    N = len(arr)

    left = 0
    right = N - 1
    idx = N

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] <= target:
            left = mid + 1
        else:
            idx = min(idx, mid)
            right = mid - 1

    return idx

def get_lower(arr, target):
    N = len(arr)

    left = 0
    right = N - 1
    idx = N

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] >= target:
            idx = min(mid, idx)
            right = mid - 1
        else:
            left = mid + 1

    return idx

def solve():
    N, M = map(int, input().split())
    dots = list(map(int, input().split()))
    lines = list(tuple(map(int, input().split())) for _ in range(M))

    dots.sort()

    for x, y in lines:
        upper = get_upper(dots, y)
        lower = get_lower(dots, x)

        print(f"{upper-lower}\n")

    return


if __name__ == "__main__":
    solve()
