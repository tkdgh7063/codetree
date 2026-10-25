import sys

input = sys.stdin.readline
print = sys.stdout.write

def get_lower(nums, target):
    N = len(nums)

    left = 0
    right = N - 1
    min_idx = N

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] >= target:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1

    return min_idx

def get_upper(nums, target):
    N = len(nums)

    left = 0
    right = N - 1
    min_idx = N

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] > target:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1

    return min_idx

def solve():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    queries = list(int(input()) for _ in range(M))

    for query in queries:
        upper_bound = get_upper(nums, query)
        lower_bound = get_lower(nums, query)
        print(str(upper_bound - lower_bound) + "\n")

    return

if __name__ == "__main__":
    solve()
