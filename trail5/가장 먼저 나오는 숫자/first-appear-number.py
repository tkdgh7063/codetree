import sys

input = sys.stdin.readline
# print = sys.stdout.write

def get_first(nums, target):
    N = len(nums)

    left = 0
    right = N - 1
    min_idx = N
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1
        else:
            min_idx = min(mid, min_idx)
            right = mid - 1

    return min_idx + 1 if min_idx != N and nums[min_idx] == target else -1

def solve():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    for query in queries:
        idx = get_first(nums, query)
        print(idx)

if __name__ == "__main__":
    solve()
